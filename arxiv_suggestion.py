# --------------------------------------------------------
# We employ "naive Bayes algorithm" (NB for short). For it, c.f.
# _Machine Learning_ by T. Mitchell, section 6.10, esp. table 6-2.
# --------------------------------------------------------
# Notation:
#   pre_prob -> prior probability
#   post_prob -> posterior probability
#   True -> like it
#   False -> dislike it
#
# We suppose the effective lengh is 5000, that is, there're
# 5000 common words in English.
# --------------------------------------------------------


# You need to ensure that the following packages
# have been installed. If not, you can, e.g.,
# `pacman -S python-urllib python-feedparser python-string`
import urllib.request, feedparser, string
from copy import copy
from math import log

# ============== Initialize ===============
# Everytime you import `arxiv_suggestion`,
# the `like_papers` is initialized as:
like_papers = {'True': [], 'False': []}

def read_personal_data():
    """ None -> Personal_data
    """
    pd = open('personal_data', 'r')
    pd_str = pd.read()
    personal_data = eval(pd_str)
    pd.close()
    return personal_data

personal_data = read_personal_data()

# ============== Parser ===============

feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'
# where we followed the parser-example provided by arXiv API website.

def get_entries(search_query, id_list, start, max_results):
    """ Str * [Str] * Int * Int -> [Entry]
    """
    def id_list_str(id_list):
        """ [Str] -> Str
        """
        result = ''
        for paper_id in id_list:
            result += (paper_id + ',')
        result = result[: -1] # remove the final ','
        return result
    def adjust_id(entries):
        """ [Entry] -> None
            Not a function -- modifies entries in outer frame.
        
        Note: `entry.id` returns, e.g.: 'http://arxiv.org/abs/_arxiv_id_'.
              So, we'd like call `entry.id[21:]` instead to drop the
              useless prefix 'http://arxiv.org/abs/'. And the last two
              chars are for version, e.g. `v1`, which we also drop. So,
              totally, we shall call `entry.id[21: -2]`.
        """
        for entry in entries:
            entry.id = entry.id[21: -2]
        return None
    base_url = 'http://export.arxiv.org/api/query?'
    query = 'search_query=%s&id_list=%s&start=%i&max_results=%i&sortBy=lastUpdatedDate&sortOrder=descending' % (search_query, id_list_str(id_list), start, max_results)
    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()
    # parse the response using feedparser
    feed = feedparser.parse(response)
    adjust_id(feed.entries)
    return feed.entries

# ============== Adjust for NB ===============

def drop_punctuation(str0):
    """ Str -> Str
    """
    exclude = set(string.punctuation)
    result = ''.join(char for char in str0 if char not in exclude)
    return result

# Exclude 100 most frequent words in English. The following words are from WikiPedia.
most_freq_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']
# and some words are also needed to be removed:
most_freq_words += ['is', 'are']

def adjust_entry(entry0):
    """ Entry -> Entry
    
    where in the summary of the new Entry, we have:
    i)   change words to their lowercase;
    ii)  split summary-texts into lists of words;
    iii) drop punctuation in words;
    iv)  drop most frequent words in English.
    """
    entry = copy(entry0)
    entry.summary = entry.summary.lower()
    entry.summary = entry.summary.split()
    entry.summary = [drop_punctuation(word) for word in entry.summary]
    entry.summary = [word for word in entry.summary if word not in most_freq_words]
    return entry

def adjust_entries(entries):
    """ [Entry] -> [Entry]
    """
    return [adjust_entry(entry) for entry in entries]

# ============== Personal Data ===============
def initialize_personal_data():
    """ -> Personal_data
    
    Personal_data = {'vocabulary': Vocabulary,
                     'like_papers': {'True': [Str], 'False': [Str]}
                     'total_words': {'True': Int, 'False': Int}}
    wherein 'total_words' is essential for updating word_frequency in 'vocabulary'.
    
    Initially, they are all empty. Vanishing `total_words` will makes error in
    compute nb_probability by initialized personal_data.
    """
    personal_data = {'vocabulary': {},
                     'like_papers': {'True': [], 'False': []},
                     'total_words': {'True': 0, 'False': 0}}
    return personal_data

def update_personal_data():
    """ None -> None
        Not a function -- changes the `personal_data` in outer frame
    """
    def update_prob(prob, n, n_update, n_word_update):
        return ((n + 5000) * prob + n_word_update) / (n + n_update + 5000)
    def initialize_word(n):
        return {'True': 1 / (n + 5000), 'False': 1 / (n + 5000)}
    def update_vocabulary(likeQ, adjusted_entries):
        text_update = []
        for entry in adjusted_entries:
            text_update += entry.summary
        n = personal_data['total_words'][str(likeQ)]
        n_update = len(text_update)
        for word in text_update:
            n_word_update = text_update.count(word)
            if word not in personal_data['vocabulary']:
                personal_data['vocabulary'][word] = initialize_word(n)
            prob = personal_data['vocabulary'][word][str(likeQ)]
            personal_data['vocabulary'][word][str(likeQ)] = update_prob(prob, n, n_update, n_word_update)
        return None
    def update_like_papers(likeQ):
        for paper_id in like_papers[str(likeQ)]:
            personal_data['like_papers'][str(likeQ)].append(paper_id)
        return None
    def update_total_words(likeQ, adjusted_entries):
        personal_data['total_words'][str(likeQ)] += sum([len(entry.summary) for entry in adjusted_entries])
    for likeQ in [True, False]:
        id_list = like_papers[str(likeQ)]
        adjusted_entries = adjust_entries(get_entries('', id_list, 0, len(id_list)))
        update_vocabulary(likeQ, adjusted_entries)
        update_like_papers(likeQ)
        update_total_words(likeQ, adjusted_entries)
    return None


# ============== Suggestion ===============

def log_post_prob(entry, likeQ, personal_data):
    """ Entry * Boolean * Personal_data -> Real
    
    Herein we employ log to enhance the computation
    accurancy. Or, bugs raise because of low accurancy.
    """
    def num_docs(likeQ):
        """ Boolean -> Int
        """
        return len(personal_data['like_papers'][str(likeQ)])
    def log_pri_prob(likeQ):
        """ Boolean -> Real
        """
        num_total_docs = num_docs(True) + num_docs(False)
        # add `0.1` for avoiding `like = []`, on which log(0) is not defined:
        return log(num_docs(likeQ) + 0.1) - log(num_total_docs + 0.1)
    def log_prob(word, likeQ):
        """ Str * Boolean -> Real
        """
        if word in personal_data['vocabulary']:
            return log(personal_data['vocabulary'][word][str(likeQ)])
        else:
            return -log(personal_data['total_words'][str(likeQ)] + 5000)
    text = adjust_entry(entry).summary
    return log_pri_prob(likeQ) + sum([log_prob(word, likeQ) for word in text])

def log_post_prob_ratio(entry, personal_data):
    """ Entry * Personal_data -> Real
    """
    return log_post_prob(entry, True , personal_data) - log_post_prob(entry, False, personal_data)



# ============== Interactive ===============

def write_personal_data():
    """ None -> None
        Not a function -- modifies `./personal_data`
    """
    f = open('personal_data', 'w')
    f.write(str(personal_data))
    f.close()
    return None

def show_entry(entry):
    """ Entry -> 
    """
    print("-------------------------")
    print("Title: ", entry.title)
    print("Authors: ", ''.join([item['name'] + ', ' for item in entry.authors])[:-2])
    print("arXiv id: ", entry.id)
    print("Summary: ", entry.summary)
    print("-------------------------")
    print()


def sort_by_func(lst, func):
    """ [a] * (a -> Real) -> [b]
        
    Default is descent.
    """
    lst_reconstruct = [(func(item), item) for item in lst]
    get_key = lambda item: item[0]
    sorted_lst = sorted(lst_reconstruct, key = get_key, reverse=True)
    result = [item[1] for item in sorted_lst]
    return result

def sort_entries_by_nb(entries, personal_data):
    """ [Entry] -> [Entry]
    """
    func = lambda entry: log_post_prob_ratio(entry, personal_data)
    entries_sorted = sort_by_func(entries, func)
    return entries_sorted   

def label(id_list, likeQ):
    """ [Str] * Boolean -> None
        Not a function -- modifies `like_papers` in outer frame
    """
    if likeQ:
        for paper_id in id_list:
            like_papers['True'].append(paper_id)
    else:
        for paper_id in id_list:
            like_papers['False'].append(paper_id)
    return None

def read_arxiv(search_query, start = 0, max_results = 10):
    """ Str * Int (=0) * Int (=10) -> None
    """
    personal_data = read_personal_data()
    entries = get_entries(search_query, [], start, max_results)
    entries_sorted = sort_entries_by_nb(entries, personal_data)
    for entry in entries_sorted:
        show_entry(entry)
        input_str = input('Are you interested in this paper?')
        if input_str == 'y': # do like this paper
            label([entry.id], True)
        elif input_str == 'n': # do not
            label([entry.id], False)
        elif input_str == 'b': # want to break
            break
    update_personal_data()
    return None
