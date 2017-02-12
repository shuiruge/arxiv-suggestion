arxiv-suggestion
=========

Give everyday suggestion of papers on arxiv.org, sorted in the order that the upper papers are regarded as interesting to you. "Naive Bayes algorithm" is employed. Written by Python3.

The following is a simple instance.

---


```python
import arxiv_suggestion as axs
```

## Personal Data

### Initialize Your Personal Data if You Have None


```python
## Run this if your personal_data is empty.
## But generally it's not.
#
personal_data = axs.initialize_personal_data()
pd = open('personal_data', 'w')
pd.write(str(personal_data))
pd.close()
```

Now my personal_data has been initialized to be empty.


```python
personal_data = axs.read_personal_data()
personal_data
```




    {'disliked_papers': [],
     'liked_papers': [],
     'total_words': {'dislike': 0, 'like': 0},
     'vocabulary': {}}



### Update Your Personal Data

Suppose I like all the recent (ten) papers written by Polchinski. Then, by employing `axs.label`, I can append their arXiv_id into `axs.liked_papers` which has been initialized as `[]`. Doing so by hand in this case (I like all of them!) is dull. Instead, we can use `


```python
liked = [entry.id for entry in axs.get_entries('au:Polchinski', [], 0, 10)]
print(liked)
```

    ['1611.04650', '1609.04036', '1602.06422', '1601.06145', '1601.06768', '1512.02477', '1509.05710', '1501.06577', '1402.6334', '1402.6327']



```python
axs.label(liked, True) # `True` means you like the paper_list. `False` means you don't.
print(axs.liked_papers)
print(axs.disliked_papers)
```

    ['1611.04650', '1609.04036', '1602.06422', '1601.06145', '1601.06768', '1512.02477', '1509.05710', '1501.06577', '1402.6334', '1402.6327']
    []


Now I can update my information by `axs.update()`, which will update my personal data in `./personal_data` by `axs.liked_papers` and `axs.disliked_papers` just `label`ed.


```python
axs.update()
```

Now, `./personal_data` is updated, as you can check.


```python
personal_data = axs.read_personal_data()
```

## Read arXiv


```python
axs.read_arxiv('cat:gr-qc', 0, 5)
```

    -------------------------
    Title:  What is the Magnetic Weak Gravity Conjecture for Axions?
    Authors:  Arthur Hebecker, Philipp Henkenjohann, Lukas T. Witkowski
    arXiv id:  1701.06553
    Summary:  The electric Weak Gravity Conjecture demands that axions with large decay
    constant $f$ couple to light instantons. The resulting large instantonic
    corrections pose problems for natural inflation. We explore an alternative
    argument based on the magnetic Weak Gravity Conjecture for axions, which we try
    to make more precise. Roughly speaking, it demands that the minimally charged
    string coupled to the dual 2-form-field exists in the effective theory. Most
    naively, such large-$f$ strings curve space too much to exist as static
    solutions, thus ruling out large-$f$ axions. More conservatively, one might
    allow non-static string solutions to play the role of the required charged
    objects. In this case, topological inflation would save the superplanckian
    axion. Furthermore, a large-$f$ axion may appear in the low-energy effective
    theory based on two subplanckian axions in the UV. The resulting effective
    string is a composite object built from several fundamental strings and domain
    walls. It may or may not satisfy the magnetic Weak Gravity Conjecture depending
    on how strictly the latter is interpreted and on the cosmological dynamics of
    this composite object, which remain to be fully understood. Finally, we recall
    that large-field brane inflation is naively possible in the codimension-one
    case. We show how string-theoretic back-reaction closes this apparent loophole
    of large-$f$ (non-periodic) pseudo-axions.
    -------------------------
    
    -------------------------
    Title:  Gravitational Coupling from Active Gravity
    Authors:  Tao Lei, Zi-Wei Chen, Zhen-Lai Wang, Xiang-Song Chen
    arXiv id:  1702.02921
    Summary:  We attempt to construct a gravitational coupling by pre-selecting an
    energy-momentum tensor as the source for gravitational field. The
    energy-momentum tensor we take is a recently derived new expression motivated
    by joint localization of energy and momentum in quantum measurement. This
    energy-momentum tensor differs from the traditional canonical and symmetric
    ones, and the theory we obtain is of an Einstein-Cartan type, but derived from
    a minimal coupling of a Lagrangian with second-derivative, and leads to
    additional interaction between torsion and matter, including the scalar field.
    For the scalar field, the theory can also be derived in the Riemann space-time
    by a non-minimal coupling. Our study gives hint on more general tests of
    general relativistic effects.
    -------------------------
    
    -------------------------
    Title:  Smoothing expansion rate data to reconstruct cosmological matter
      perturbations
    Authors:  J. E. Gonzalez, J. S. Alcaniz, J. C. Carvalho
    arXiv id:  1702.02923
    Summary:  The existing degeneracy between different dark energy and modified gravity
    cosmologies at the background level may be broken by analysing quantities at
    the perturbative level. In this work, we apply a non-parametric smoothing (NPS)
    method to reconstruct the expansion history of the Universe ($H(z)$) from
    model-independent cosmic chronometers and high-$z$ quasar data. Assuming a
    homogeneous and isotropic flat universe and general relativity (GR) as the
    gravity theory, we calculate the non-relativistic matter perturbations in the
    linear regime using the $H(z)$ reconstruction and realistic values of
    $\Omega_{m0}$ and $\sigma_8$ from Planck and WMAP-9 collaborations. We find a
    good agreement between the measurements of the growth rate and $f\sigma_8(z)$
    from current large-scale structure observations and the estimates obtained from
    the reconstruction of the cosmic expansion history. Considering a recently
    proposed null test for GR using matter perturbations, we also apply the NPS
    method to reconstruct $f\sigma_8(z)$. For this case, we find a $\sim 2\sigma$
    tension (good agreement) with the standard relativistic cosmology when the
    Planck (WMAP-9) priors are used.
    -------------------------
    
    -------------------------
    Title:  Yang-Baxter $σ$-models, conformal twists & noncommutative
      Yang-Mills
    Authors:  T. Araujo, I. Bakhmatov, E. Ó Colgáin, J. Sakamoto, M. M. Sheikh-Jabbari, K. Yoshida
    arXiv id:  1702.02861
    Summary:  The Yang-Baxter $\sigma$-model is a systematic way to generate integrable
    deformations of AdS$_5\times$S$^5$. We recast the deformations as seen by open
    strings, where the metric is undeformed AdS$_5\times$S$^5$ with constant string
    coupling, and all information about the deformation is encoded in the
    noncommutative (NC) parameter $\Theta$. We identify the deformations of AdS$_5$
    as twists of the conformal algebra, thus explaining the noncommutativity. We
    show that the unimodularity conditon on $r$-matrices for supergravity solutions
    translates into $\Theta$ being divergence-free. Integrability of the
    $\sigma$-model for unimodular $r$-matrices implies the existence and planar
    integrability of the dual NC gauge theory.
    -------------------------
    
    -------------------------
    Title:  Reissner-Nordstrøm-de Sitter Manifold : Photon Sphere and Maximal
      Analytic Extension
    Authors:  Mokdad Mokdad
    arXiv id:  1701.06982
    Summary:  This paper is devoted to the study of the Reissner-Nordstr{\o}m-de Sitter
    black holes and their maximal analytic extensions. In particular, we study some
    of their properties that lays the groundwork for separate papers where we
    obtain decay results and construct conformal scattering theories for test
    fields on such spacetimes. Here, we find the necessary and sufficient
    conditions on the parameters of the Reissner-Nordstr{\o}m-de Sitter metric
    -namely, the mass, the charge, and the cosmological constant- to have three
    horizons. Under this conditions, we prove that there is only one photon sphere
    and we locate it. We then give a detailed construction of the maximal analytic
    extension of the Reissner-Nordstr{\o}m-de Sitter manifold in the case of three
    horizons.
    -------------------------
    


where in `axs.read_arxiv`, we have sorted the order of shown up papers by NB. Indeed, we can print out the un-sorted, by:


```python
entries = axs.get_raw_entries('cat:gr-qc', [], 0, 5)
for entry in entries:
    axs.show_entry(entry)
```

    -------------------------
    Title:  Smoothing expansion rate data to reconstruct cosmological matter
      perturbations
    Authors:  J. E. Gonzalez, J. S. Alcaniz, J. C. Carvalho
    arXiv id:  1702.02923
    Summary:  The existing degeneracy between different dark energy and modified gravity
    cosmologies at the background level may be broken by analysing quantities at
    the perturbative level. In this work, we apply a non-parametric smoothing (NPS)
    method to reconstruct the expansion history of the Universe ($H(z)$) from
    model-independent cosmic chronometers and high-$z$ quasar data. Assuming a
    homogeneous and isotropic flat universe and general relativity (GR) as the
    gravity theory, we calculate the non-relativistic matter perturbations in the
    linear regime using the $H(z)$ reconstruction and realistic values of
    $\Omega_{m0}$ and $\sigma_8$ from Planck and WMAP-9 collaborations. We find a
    good agreement between the measurements of the growth rate and $f\sigma_8(z)$
    from current large-scale structure observations and the estimates obtained from
    the reconstruction of the cosmic expansion history. Considering a recently
    proposed null test for GR using matter perturbations, we also apply the NPS
    method to reconstruct $f\sigma_8(z)$. For this case, we find a $\sim 2\sigma$
    tension (good agreement) with the standard relativistic cosmology when the
    Planck (WMAP-9) priors are used.
    -------------------------
    
    -------------------------
    Title:  Gravitational Coupling from Active Gravity
    Authors:  Tao Lei, Zi-Wei Chen, Zhen-Lai Wang, Xiang-Song Chen
    arXiv id:  1702.02921
    Summary:  We attempt to construct a gravitational coupling by pre-selecting an
    energy-momentum tensor as the source for gravitational field. The
    energy-momentum tensor we take is a recently derived new expression motivated
    by joint localization of energy and momentum in quantum measurement. This
    energy-momentum tensor differs from the traditional canonical and symmetric
    ones, and the theory we obtain is of an Einstein-Cartan type, but derived from
    a minimal coupling of a Lagrangian with second-derivative, and leads to
    additional interaction between torsion and matter, including the scalar field.
    For the scalar field, the theory can also be derived in the Riemann space-time
    by a non-minimal coupling. Our study gives hint on more general tests of
    general relativistic effects.
    -------------------------
    
    -------------------------
    Title:  What is the Magnetic Weak Gravity Conjecture for Axions?
    Authors:  Arthur Hebecker, Philipp Henkenjohann, Lukas T. Witkowski
    arXiv id:  1701.06553
    Summary:  The electric Weak Gravity Conjecture demands that axions with large decay
    constant $f$ couple to light instantons. The resulting large instantonic
    corrections pose problems for natural inflation. We explore an alternative
    argument based on the magnetic Weak Gravity Conjecture for axions, which we try
    to make more precise. Roughly speaking, it demands that the minimally charged
    string coupled to the dual 2-form-field exists in the effective theory. Most
    naively, such large-$f$ strings curve space too much to exist as static
    solutions, thus ruling out large-$f$ axions. More conservatively, one might
    allow non-static string solutions to play the role of the required charged
    objects. In this case, topological inflation would save the superplanckian
    axion. Furthermore, a large-$f$ axion may appear in the low-energy effective
    theory based on two subplanckian axions in the UV. The resulting effective
    string is a composite object built from several fundamental strings and domain
    walls. It may or may not satisfy the magnetic Weak Gravity Conjecture depending
    on how strictly the latter is interpreted and on the cosmological dynamics of
    this composite object, which remain to be fully understood. Finally, we recall
    that large-field brane inflation is naively possible in the codimension-one
    case. We show how string-theoretic back-reaction closes this apparent loophole
    of large-$f$ (non-periodic) pseudo-axions.
    -------------------------
    
    -------------------------
    Title:  Reissner-Nordstrøm-de Sitter Manifold : Photon Sphere and Maximal
      Analytic Extension
    Authors:  Mokdad Mokdad
    arXiv id:  1701.06982
    Summary:  This paper is devoted to the study of the Reissner-Nordstr{\o}m-de Sitter
    black holes and their maximal analytic extensions. In particular, we study some
    of their properties that lays the groundwork for separate papers where we
    obtain decay results and construct conformal scattering theories for test
    fields on such spacetimes. Here, we find the necessary and sufficient
    conditions on the parameters of the Reissner-Nordstr{\o}m-de Sitter metric
    -namely, the mass, the charge, and the cosmological constant- to have three
    horizons. Under this conditions, we prove that there is only one photon sphere
    and we locate it. We then give a detailed construction of the maximal analytic
    extension of the Reissner-Nordstr{\o}m-de Sitter manifold in the case of three
    horizons.
    -------------------------
    
    -------------------------
    Title:  Yang-Baxter $σ$-models, conformal twists & noncommutative
      Yang-Mills
    Authors:  T. Araujo, I. Bakhmatov, E. Ó Colgáin, J. Sakamoto, M. M. Sheikh-Jabbari, K. Yoshida
    arXiv id:  1702.02861
    Summary:  The Yang-Baxter $\sigma$-model is a systematic way to generate integrable
    deformations of AdS$_5\times$S$^5$. We recast the deformations as seen by open
    strings, where the metric is undeformed AdS$_5\times$S$^5$ with constant string
    coupling, and all information about the deformation is encoded in the
    noncommutative (NC) parameter $\Theta$. We identify the deformations of AdS$_5$
    as twists of the conformal algebra, thus explaining the noncommutativity. We
    show that the unimodularity conditon on $r$-matrices for supergravity solutions
    translates into $\Theta$ being divergence-free. Integrability of the
    $\sigma$-model for unimodular $r$-matrices implies the existence and planar
    integrability of the dual NC gauge theory.
    -------------------------
    


