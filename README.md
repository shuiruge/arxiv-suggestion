arxiv-suggestion
=========

Description
---------
Give everyday suggestion of papers on arxiv.org, sorted in the order that the upper papers are regarded as interesting to you. "Naive Bayes algorithm" is employed. Written by Python3.

Motivation
---------
When I was doing my research on physics (inflation), I had to read arXiv in every morning, viewing papers in categories: astro-ph, gr-qc, and hep-th. In fact, among almost 100 papers, only several papers are interesting to me. It would benefit a lot if papers are in an order that those several papers interesting to me are shown at the top. Indeed, several website, e.g. feedly.com, does show up three hot papers every time you read. But not enough. Importantly, I want to make such sorting be personalized. That is, only use the data of reading of **mine**! So, I wrote this tiny programme, hoping that it will benefit you also.

Example
------

The following is a simple instance. You can following this pattern of usage, make it your own.

---

Ensure that you're using Python3, rather than Python2. To start, just type `python3` in your terminal. And then,

```python
import arxiv_suggestion as axs
```

## Personal Data

### Initialize Your Personal Data

If you have used `arxiv_suggestion` and have well trained personal data, please skip this section. But, if this is your first time, you shall initialize your personal data, by


```python
axs.personal_data = axs.initialize_personal_data()
axs.write_personal_data()
```

Now my personal_data has been initialized to be empty, as


```python
personal_data = axs.read_personal_data()
personal_data
```




    {'like_papers': {'False': [], 'True': []},
     'total_words': {'False': 0, 'True': 0},
     'vocabulary': {}}



## Reading arXiv while Updating Your Personal Data

`axs.read_arxiv` sorts papers in the order that the papers are regarded as interesting to you, suggested by NB. Your data is read from `./personal_data`. If you do be interested in it, type `y`; if not, type `n`; if you do not know, type `Enter`; and if you want to break, type `b`. In the end, it will update your personal data, but will not write your updated personal data into `./personal_data`.


```python
help(axs.read_arxiv)
```

    Help on function read_arxiv in module arxiv_suggestion:
    
    read_arxiv(search_query, start=0, max_results=10)
        Str * Int (=0) * Int (=10) -> None
    


Suppose you want to read the newest 3 papers in category "gr-qc", you shall set `search_query` as `cat:gr-qc`, demanded by arXiv API, `start` as `0`, and `max_results` as `3`. That is, `axs.read_arxiv('cat:gr-qc', 0, 3)`. Then, papers are shown one by one. In the end of each paper, you are to asked to label it as interesting or not, or just passing it. So,


```python
axs.read_arxiv('cat:gr-qc', 0, 3)
```

    
    -------------------------
    Title:  Horizonless, singularity-free, compact shells satisfying NEC
    Authors:  Karthik H. Shankar
    Update Data:  2017-02-16T18:33:50Z
    Link:  http://arxiv.org/abs/1510.00851v2
    Summary:  Gravitational collapse singularities are undesirable, yet inevitable to a
    large extent in General Relativity. When matter satisfying null energy
    condition collapses to the extent a closed trapped surface is formed, a
    singularity is inevitable according to Penrose's singularity theorem. Since
    positive mass vacuum solutions are generally black holes with trapped surfaces
    inside the event horizon, matter cannot collapse to an arbitrarily small size
    without generating a singularity. However, in modified theories of gravity
    where positive mass vacuum solutions are naked singularities with no trapped
    surfaces, it is reasonable to expect that matter can collapse to an arbitrarily
    small size without generating a singularity. Here we examine this possibility
    in the context of a modified theory of gravity with torsion in an extra
    dimension. We study singularity-free static shell solutions to evaluate the
    validity of the null energy condition on the shell. We find that with
    sufficiently high pressure, matter can be collapsed to arbitrarily small size
    without violating the null energy condition and without producing a
    singularity.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)y
    
    -------------------------
    Title:  Towards Strong Field Tests of Beyond Horndeski Gravity Theories
    Authors:  Jeremy Sakstein, Eugeny Babichev, Kazuya Koyama, David Langlois, Ryo Saito
    Update Data:  2017-02-16T18:30:32Z
    Link:  http://arxiv.org/abs/1612.04263v2
    Summary:  Theories of gravity in the beyond Horndeski class encompass a wide range of
    scalar-tensor theories that will be tested on cosmological scales over the
    coming decade. In this work, we investigate the possibility of testing them in
    the strong-field regime by looking at the properties of compact
    objects-neutron, hyperon, and quark stars-embedded in an asymptotically de
    Sitter space-time, for a specific subclass of theories. We extend previous
    works to include slow rotation and find a relation between the dimensionless
    moment of intertia, ($\bar{I}=Ic^2/G_{\rm N} M^3$), and the compactness,
    $\cal{C}=G_{\rm N} M/Rc^2$ (an $\bar{I}$-$\cal{C}$ relation), independent of
    the equation of state, that is reminiscent of but distinct from the general
    relativity prediction. Several of our equations of state contain hyperons and
    free quarks, allowing us to revisit the hyperon puzzle. We find that the
    maximum mass of hyperon stars can be larger than $2M_\odot$ for small values of
    the beyond Horndeski parameter, thus providing a resolution of the hyperon
    puzzle based on modified gravity. Moreover, stable quark stars exist when
    hyperonic stars are unstable, which means that the phase transition from
    hyperon to quark stars is predicted just as in general relativity, albeit with
    larger quark star masses. Two important and potentially observable consequences
    of some of the theories we consider are the existence of neutron stars in a
    range of masses significantly higher than in GR, and $\bar{I}$-$\mathcal{C}$
    relations that differ from their GR counterparts. In the former case, we find
    objects that, if observed, could not be accounted for in GR because they
    violate the usual GR causality condition. We end by discussing several
    difficult technical issues that remain to be addressed in order to reach more
    realistic predictions that may be tested using gravitational wave searches or
    neutron star observations.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)n
    
    -------------------------
    Title:  3D Simulation of Spindle Gravitational Collapse of a Collisionless
      Particle System
    Authors:  Chul-Moon Yoo, Tomohiro Harada, Hirotada Okawa
    Update Data:  2017-02-16T18:13:24Z
    Link:  http://arxiv.org/abs/1611.07906v2
    Summary:  We simulate the spindle gravitational collapse of a collisionless particle
    system in a 3D numerical relativity code and compare the qualitative results
    with the old work done by Shapiro and Teukolsky(ST). The simulation starts from
    the prolate-shaped distribution of particles and a spindle collapse is
    observed. The peak value and its spatial position of curvature invariants are
    monitored during the time evolution. We find that the peak value of the
    Kretschmann invariant takes a maximum at some moment, when there is no apparent
    horizon, and its value is greater for a finer resolution, which is consistent
    with what is reported in ST. We also find a similar tendency for the Weyl
    curvature invariant. Therefore, our results lend support to the formation of a
    naked singularity as a result of the axially symmetric spindle collapse of a
    collisionless particle system in the limit of infinite resolution. However,
    unlike in ST, our code does not break down then but go well beyond.We find that
    the peak values of the curvature invariants start to gradually decrease with
    time for a certain period of time. Another notable difference from ST is that,
    in our case, the peak position of the Kretschmann curvature invariant is always
    inside the matter distribution.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)


Now, `axs.like_papers` labels your new interests.


```python
print(axs.like_papers)
```

    {'True': ['1510.00851'], 'False': ['1612.04263']}


In addition, since your personal data has been updated by `axs.read_arxiv`, you will have


```python
axs.personal_data['like_papers']
```




    {'False': ['1612.04263'], 'True': ['1510.00851']}



Then we write the updated `personal_data` into `./personal_data` to update your training data.


```python
axs.write_personal_data()
```

Then, we have


```python
axs.read_arxiv('cat:gr-qc', 0, 5)
```

    
    -------------------------
    Title:  Horizonless, singularity-free, compact shells satisfying NEC
    Authors:  Karthik H. Shankar
    Update Data:  2017-02-16T18:33:50Z
    Link:  http://arxiv.org/abs/1510.00851v2
    Summary:  Gravitational collapse singularities are undesirable, yet inevitable to a
    large extent in General Relativity. When matter satisfying null energy
    condition collapses to the extent a closed trapped surface is formed, a
    singularity is inevitable according to Penrose's singularity theorem. Since
    positive mass vacuum solutions are generally black holes with trapped surfaces
    inside the event horizon, matter cannot collapse to an arbitrarily small size
    without generating a singularity. However, in modified theories of gravity
    where positive mass vacuum solutions are naked singularities with no trapped
    surfaces, it is reasonable to expect that matter can collapse to an arbitrarily
    small size without generating a singularity. Here we examine this possibility
    in the context of a modified theory of gravity with torsion in an extra
    dimension. We study singularity-free static shell solutions to evaluate the
    validity of the null energy condition on the shell. We find that with
    sufficiently high pressure, matter can be collapsed to arbitrarily small size
    without violating the null energy condition and without producing a
    singularity.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)
    
    -------------------------
    Title:  3D Simulation of Spindle Gravitational Collapse of a Collisionless
      Particle System
    Authors:  Chul-Moon Yoo, Tomohiro Harada, Hirotada Okawa
    Update Data:  2017-02-16T18:13:24Z
    Link:  http://arxiv.org/abs/1611.07906v2
    Summary:  We simulate the spindle gravitational collapse of a collisionless particle
    system in a 3D numerical relativity code and compare the qualitative results
    with the old work done by Shapiro and Teukolsky(ST). The simulation starts from
    the prolate-shaped distribution of particles and a spindle collapse is
    observed. The peak value and its spatial position of curvature invariants are
    monitored during the time evolution. We find that the peak value of the
    Kretschmann invariant takes a maximum at some moment, when there is no apparent
    horizon, and its value is greater for a finer resolution, which is consistent
    with what is reported in ST. We also find a similar tendency for the Weyl
    curvature invariant. Therefore, our results lend support to the formation of a
    naked singularity as a result of the axially symmetric spindle collapse of a
    collisionless particle system in the limit of infinite resolution. However,
    unlike in ST, our code does not break down then but go well beyond.We find that
    the peak values of the curvature invariants start to gradually decrease with
    time for a certain period of time. Another notable difference from ST is that,
    in our case, the peak position of the Kretschmann curvature invariant is always
    inside the matter distribution.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)
    
    -------------------------
    Title:  A pseudo-Newtonian Hamiltonian for test motion in stationary space-times
    Authors:  Vojtech Witzany, Claus Laemmerzahl
    Update Data:  2017-02-16T17:51:16Z
    Link:  http://arxiv.org/abs/1601.01034v2
    Summary:  Pseudo-Newtonian potentials are a tool often used in theoretical astrophysics
    to capture some key features of a black-hole space-time in a Newtonian
    framework. As a result, one can use Newtonian numerical codes, and Newtonian
    formalism in general, in an effective description of important astrophysical
    processes such as accretion onto black holes.
      In this paper we develop a general pseudo-Newtonian formalism which pertains
    to the motion of particles, light, and fluids in stationary space-times. In
    return, we are able to assess the applicability of the pseudo-Newtonian scheme.
    The simplest and most elegant formulas are obtained in space-times without
    gravitomagnetic effects, such as the Schwarzschild rather than the Kerr
    space-time; the quantitative errors are smallest for motion with low binding
    energy. Included is a ready-to-use set of fluid equations in Schwarzschild
    space-time in Cartesian coordinates.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)
    
    -------------------------
    Title:  Impact of the latest measurement of Hubble constant on constraining
      inflation models
    Authors:  Xin Zhang
    Update Data:  2017-02-16T15:28:37Z
    Link:  http://arxiv.org/abs/1702.05010v1
    Summary:  This is a Letter to the Editor of SCIENCE CHINA Physics, Mechanics &
    Astronomy.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)
    
    -------------------------
    Title:  Towards Strong Field Tests of Beyond Horndeski Gravity Theories
    Authors:  Jeremy Sakstein, Eugeny Babichev, Kazuya Koyama, David Langlois, Ryo Saito
    Update Data:  2017-02-16T18:30:32Z
    Link:  http://arxiv.org/abs/1612.04263v2
    Summary:  Theories of gravity in the beyond Horndeski class encompass a wide range of
    scalar-tensor theories that will be tested on cosmological scales over the
    coming decade. In this work, we investigate the possibility of testing them in
    the strong-field regime by looking at the properties of compact
    objects-neutron, hyperon, and quark stars-embedded in an asymptotically de
    Sitter space-time, for a specific subclass of theories. We extend previous
    works to include slow rotation and find a relation between the dimensionless
    moment of intertia, ($\bar{I}=Ic^2/G_{\rm N} M^3$), and the compactness,
    $\cal{C}=G_{\rm N} M/Rc^2$ (an $\bar{I}$-$\cal{C}$ relation), independent of
    the equation of state, that is reminiscent of but distinct from the general
    relativity prediction. Several of our equations of state contain hyperons and
    free quarks, allowing us to revisit the hyperon puzzle. We find that the
    maximum mass of hyperon stars can be larger than $2M_\odot$ for small values of
    the beyond Horndeski parameter, thus providing a resolution of the hyperon
    puzzle based on modified gravity. Moreover, stable quark stars exist when
    hyperonic stars are unstable, which means that the phase transition from
    hyperon to quark stars is predicted just as in general relativity, albeit with
    larger quark star masses. Two important and potentially observable consequences
    of some of the theories we consider are the existence of neutron stars in a
    range of masses significantly higher than in GR, and $\bar{I}$-$\mathcal{C}$
    relations that differ from their GR counterparts. In the former case, we find
    objects that, if observed, could not be accounted for in GR because they
    violate the usual GR causality condition. We end by discussing several
    difficult technical issues that remain to be addressed in order to reach more
    realistic predictions that may be tested using gravitational wave searches or
    neutron star observations.
    -------------------------
    Are you interested in this paper?
    (If yes, type y; else if no, type n; else type Enter. Type b for break.)


Comparing with


```python
axs.read_personal_data()['like_papers']
```




    {'False': ['1612.04263'], 'True': ['1510.00851']}



we find that the one liked paper is shown in the top, while the one disliked paper is shown in the bottom, as it shall be.

### Update Your Personal Data in One Go

You can update your personal training data in the above way. But, you can make it in one go. For instance, suppose you like all the recent (ten) papers written by Polchinski (as a big fan). Then, by employing `axs.label`, I can append their arXiv_id into `axs.liked_papers` which has been initialized as `[]`. Doing so by hand in this case (I like all of them!) is dull. Instead, you can use `


```python
liked = [entry.id for entry in axs.get_entries('au:Polchinski', [], 0, 10)]
print(liked)
```

    ['1611.04650', '1609.04036', '1602.06422', '1601.06145', '1601.06768', '1512.02477', '1509.05710', '1501.06577', '1402.6334', '1402.6327']


Then you can `label` them as liked, that is as `True`.


```python
axs.label(liked, True)
print(axs.like_papers)
```

    {'True': ['1510.00851', '1611.04650', '1609.04036', '1602.06422', '1601.06145', '1601.06768', '1512.02477', '1509.05710', '1501.06577', '1402.6334', '1402.6327'], 'False': ['1612.04263']}


Now you can update your personal data by `axs.update_personal_data()`, which will update your personal data by just `label`ed. And then write it into `./personal_data`.


```python
axs.update_personal_data()
axs.write_personal_data()
```

Now, `./personal_data` is updated, as you can check.


```python
personal_data = axs.read_personal_data()
print(personal_data['like_papers'])
```

    {'True': ['1510.00851', '1611.04650', '1609.04036', '1602.06422', '1601.06145', '1601.06768', '1512.02477', '1509.05710', '1501.06577', '1402.6334', '1402.6327'], 'False': ['1612.04263']}

