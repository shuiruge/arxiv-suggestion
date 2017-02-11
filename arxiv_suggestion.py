# --------------------------------------------------------
# We employ "naive Bayes algorithm" (NB for short). For it, c.f.
# _Machine Learning_ by T. Mitchell, section 6.10, esp. table 6-2.
# --------------------------------------------------------

# Everytime you import `arxiv_suggestion`, the `liked_papers`
# and the `disliked_papers` are initialized, as:
liked_papers = []
disliked_papers = []

# You need to ensure that the following packages
# have been installed. If not, you can, e.g.,
# `pacman -S python-urllib python-feedparser python-string`
import urllib.request, feedparser, string
from copy import copy
from math import log, exp

# ============== Parser ===============
feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'
# where we followed the parser-example provided by arXiv API website.

def get_raw_entries(search_query, id_list, start, max_results):
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
def adjust_raw_entries(raw_entries):
    """ [Raw_entry] -> [Entry]
    
    where in the summary of the new Entry, we have:
    i)   change words to their lowercase;
    ii)  split summary-texts into lists of words;
    iii) drop punctuation in words;
    iv)  drop most frequent words in English.
    """
    entries = copy(raw_entries)
    for entry in entries:
        entry.summary = entry.summary.lower()
        entry.summary = entry.summary.split()
        entry.summary = [drop_punctuation(word) for word in entry.summary]
        entry.summary = [word for word in entry.summary if word not in most_freq_words]
    return entries

def get_entries(search_query, id_list, start, max_results):
    """ Str * [Str] * Int * Int -> [Entry]
    """
    raw_entries = get_raw_entries(search_query, id_list, start, max_results)
    entries = adjust_raw_entries(raw_entries)
    return entries

# ============== Personal Data ===============
def initialize_personal_data():
    """ -> Personal_data
    
    Personal_data = {'vocabulary': Vocabulary,
                     'liked_papers': [Str],
                     'disliked_papers' [Str]
                     'total_words': {'like': Int, 'dislike': Int}}
    wherein 'total_words' is essential for updating word_frequency in 'vocabulary'.
    
    Initially, they are all empty. Vanishing `total_words` will makes error in
    compute nb_probability by initialized personal_data.
    """
    vocabulary = {}
    liked_papers = []
    disliked_papers = []
    personal_data = {'vocabulary': vocabulary,
                     'liked_papers': liked_papers,
                     'disliked_papers': disliked_papers,
                     'total_words': {'like': 0, 'dislike': 0}}
    return personal_data

def update_personal_data_by_liked(id_list, personal_data):
    """ [Str] * Personal_data -> Personal_data
    """
    personal_data_updated = initialize_personal_data()
    # key 'liked_papers':
    personal_data_updated['liked_papers'] = personal_data['liked_papers'] + id_list
    # key 'disliked_papers':
    personal_data_updated['disliked_papers'] = personal_data['disliked_papers']
    # key 'total_words':
    entries = get_entries('', id_list, 0, len(id_list))
    text_updated = []
    for entry in entries:
        text_updated += entry.summary
    n_origin = personal_data['total_words']['like']
    n_updated = n_origin + len(text_updated)
    personal_data_updated['total_words']['like'] = n_updated
    personal_data_updated['total_words']['dislike'] = personal_data['total_words']['dislike']
    # key 'vocabulary':
    vocabulary = copy(personal_data['vocabulary'])
    for word in text_updated:
        if word in vocabulary:
            n_word_origin = (n_origin + 3000) * vocabulary[word]['like'] - 1
            n_word_updated = n_word_origin + text_updated.count(word)
            vocabulary[word]['like'] = (n_word_updated + 1) / (n_updated + 3000)
        else:
            vocabulary[word] = {'like': (text_updated.count(word) + 1) / (n_updated + 3000),
                                'dislike': 1 / (n_updated + 3000)}
    personal_data_updated['vocabulary'] = vocabulary
    return personal_data_updated
def like(raw_id_list, personal_data):
    """ [Str] * Personal_data -> Personal_data
    """
    id_list = []
    for paper_id in raw_id_list:
        if paper_id not in personal_data['liked_papers']:
            id_list += [paper_id]
    if id_list != []:
        return update_personal_data_by_liked(id_list, personal_data)
    else:
        return personal_data

def update_personal_data_by_disliked(id_list, personal_data):
    """ [Str] * Personal_data -> Personal_data
    """
    personal_data_updated = initialize_personal_data()
    # key 'liked_papers':
    personal_data_updated['liked_papers'] = personal_data['liked_papers']
    # key 'disliked_papers':
    personal_data_updated['disliked_papers'] = personal_data['disliked_papers'] + id_list
    # key 'total_words':
    entries = get_entries('', id_list, 0, len(id_list))
    text_updated = []
    for entry in entries:
        text_updated += entry.summary
    n_origin = personal_data['total_words']['dislike']
    n_updated = n_origin + len(text_updated)
    personal_data_updated['total_words']['like'] = personal_data['total_words']['like']
    personal_data_updated['total_words']['dislike'] = n_updated
    # key 'vocabulary':
    vocabulary = copy(personal_data['vocabulary'])
    for word in text_updated:
        if word in vocabulary:
            n_word_origin = (n_origin + 3000) * vocabulary[word]['dislike'] - 1
            n_word_updated = n_word_origin + text_updated.count(word)
            vocabulary[word]['dislike'] = (n_word_updated + 1) / (n_updated + 3000)
        else:
            vocabulary[word] = {'like': 1 / (n_updated + 3000),
                                'dislike': (text_updated.count(word) + 1) / (n_updated + 3000)}
    personal_data_updated['vocabulary'] = vocabulary
    return personal_data_updated
def dislike(raw_id_list, personal_data):
    """ [Str] * Personal_data -> Personal_data
    """
    id_list = []
    for paper_id in raw_id_list:
        if paper_id not in personal_data['disliked_papers']:
            id_list += [paper_id]
    if id_list != []:
        return update_personal_data_by_disliked(id_list, personal_data)
    else:
        return personal_data

# ============== Suggestion ===============
def compute_log_nb_like(entry, personal_data):
    """ Entry * Personal_data -> Real
    """
    vocabulary = personal_data['vocabulary']
    n = personal_data['total_words']
    # add `0.1` for avoiding `liked_paper = []`, on which log(0) is not defined:
    log_p = log(len(personal_data['liked_papers']) + 0.1) - log((len(personal_data['liked_papers']) + len(personal_data['disliked_papers']) + 0.1))
    log_product_condition_probabilities = 0
    for word in entry.summary:
        if word in vocabulary:
            log_product_condition_probabilities += log(vocabulary[word]['like'])
        else:
            log_product_condition_probabilities += log(1 / (n['like'] + 3000))
    log_nb_like = log_p + log_product_condition_probabilities
    return log_nb_like
def compute_log_nb_dislike(entry, personal_data):
    """ Entry * Personal_data -> Real
    """ 
    vocabulary = personal_data['vocabulary']
    n = personal_data['total_words']
    # add `0.1` for avoiding `liked_paper = []`, on which log(0) is not defined:
    log_p = log(len(personal_data['disliked_papers']) + 0.1) - log((len(personal_data['liked_papers']) + len(personal_data['disliked_papers'])) + 0.1)
    log_product_condition_probabilities = 0
    for word in entry.summary:
        if word in vocabulary:
            log_product_condition_probabilities += log(vocabulary[word]['dislike'])
        else:
            log_product_condition_probabilities += log(1 / (n['dislike'] + 3000))
    log_nb_dislike = log_p + log_product_condition_probabilities
    return log_nb_dislike
def log_nb_probabilities_ratio(entry, personal_data):
    """ Entry * Personal_data -> Real
    
    'nb' for "Naive Bayes Algorithm".
    The output probability is that of likeness.
    """
    log_nb_like = compute_log_nb_like(entry, personal_data)
    log_nb_dislike = compute_log_nb_dislike(entry, personal_data)
    return log_nb_like - log_nb_dislike



# ============== Interactive ===============
def read_personal_data():
    """ None -> Personal_data
    """
    pd = open('personal_data', 'r')
    pd_str = pd.read()
    personal_data = eval(pd_str)
    pd.close()
    return personal_data

def write_personal_data(personal_data):
    """ Personal_data -> None
        Not a function -- modifies `./personal_data`
    """
    pd = open('personal_data', 'w')
    pd.write(str(personal_data))
    pd.close()
    return None

def show_entry(raw_entry):
    """ Raw_entry -> None
    """
    print("-------------------------")
    print("Title: ", raw_entry.title)
    print("Authors: ", ''.join([item['name'] + ', ' for item in raw_entry.authors])[:-2])
    print("arXiv id: ", raw_entry.id)
    print("Summary: ", raw_entry.summary)
    print("-------------------------")
    print()

def sort_entries_by_nb(entries):
    """ [Entry] -> [Entry]
    """
    personal_data = read_personal_data()
    def sort_by_first(lst):
        """ Not a function!
        """
        lst.sort()
        lst.reverse()
        return None
    lst = [[log_nb_probabilities_ratio(entry, personal_data), entry] for entry in entries]
    sort_by_first(lst)
    entries_sorted = [item[1] for item in lst]
    return entries_sorted
    
def read_arxiv(search_query, start = 0, max_results = 10):
    """ Str * Int (=0) * Int (=10) -> None
    """
    id_list = []
    entries = get_raw_entries(search_query, id_list, start, max_results)
    entries_sorted = sort_entries_by_nb(entries)
    for entry in entries_sorted:
        show_entry(entry)
    return None

def label(id_list, likeQ, lp = liked_papers, dlp = disliked_papers):
    """ [Str] * Boolean -> None
        Not a function -- changes `liked_papers` and `disliked_papers`
    """
    if likeQ:
        for paper_id in id_list:
            lp.append(paper_id)
    else:
        for paper_id in id_list:
            dlp.append(paper_id)
    return None

def update(lp = liked_papers, dlp = disliked_papers):
    """ [Str] (=liked_papers) * [Str] (=disliked_papers) -> None
        Not a function -- changes the `personal_data` file
    """
    personal_data = read_personal_data()
    def update_personal_data(liked_papers, disliked_papers):
        personal_data_updated = like(liked_papers, personal_data)
        personal_data_updated = dislike(disliked_papers, personal_data_updated)
        return personal_data_updated
    personal_data = update_personal_data(lp, dlp)
    write_personal_data(personal_data)
    return None
