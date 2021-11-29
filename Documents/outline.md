---
documentclass: article
geometry: margin=1in
fontsize: 12pt
nocite: '@*'
linkcolor: blue
header-includes:
  - \usepackage{setspace}
  - \usepackage{amsfonts}
  - \usepackage{blkarray}
  - \usepackage{booktabs}

title: How Quorum Sensing Interactions Affect Microbial Population Structures
subtitle: "02-712 Final Project"
date: \today
author:
  - name: Siddharth Reed
    affiliation: 1
    email: slreed@andrew.cmu.edu
  - name: Neel
    affiliation: 1
  - name: Evan
    affiliation: 1
  - name: Sarah
    affiliation: 1
  - name: Deepika
    affiliation: 1
institute:
  - num: 1
    name: Computational Biology Department, Carnegie Mellon University
---

# Premise

Many bacteria can change their behaviours at a population level using Quorum Sensing (QS).
By default all bacteria in a population produce a extracellular signaling molecule that all other bacteria can detect.
Once the population reaches a certain density then the signaling molecule is present in high enough concentrations it is absorbed enough by the bacteria to induce some kind of response e.g. biofilm growth, surfactin production (induces growth) etc [@eldar_2011].
These responses can benefit only signal molecule producing bacteria (kin recognition) or any microbes in the environment (public good).

Bacteria that don't produce a signaling molecule still benefit from a public good response but incur no cost from signaling or contributing to the public good.
If you get mutations it is possible for a specific bacterium to never produce the signaling molecule.
Such bacteria are called "cheaters" since they benefit/consume resources without "paying into" the public good.
Such cheater mutants can persist as they will grow faster than the WT (all gain, no pain).
Cheaters help maintain diversity in QS signaling systems as diverged incompatible QS systems are still maintained at the population level through the indiscriminate public good [@pollak_2015].

The original paper @gore_2016 from the suggestion list and a follow up to @eldar_2011,  [@pollak_2015], describe how having "cheaters" in QS systems are actually selected for is specifically observed in \textit{B. subtili}.

# Our Work

We want to see how having different sets of compatible QS interactions affect the structure of microbial populations.

Note that $K_{ac}$ represent which QS systems are compatible so for each strain $R_iS_j$ then $K_{ac}[i][j] = 1$ else $K_{ac}[i][j] = 0$
Some questions we are interested in is how does structure or QS compatibility (i.e. $K_{ac}$) affect

1. total population growth rate?
1. time until at stationary distribution?
1. difference between terminal/initial state?
   - population diversity at terminal state?
     - Final alpha/beta diversity or Bray-Curtis
   - total populations size
1. how different are simulations when using micriobime data as initial state?
   - Are certain matrices more likely to lead to a diseased state over time?
   - what if we use matrices inspired by real sets of QS systems?

## TODO

So our tasks would involve

1. We implement the model described in @eldar_2011
   - ideally we use actual python ODE solvers for efficiency/accuracy reasons
   - stopping conditions is either set time limit or reaching a stationary distribution
   - develop a "null" model to compare against
     - I think $K_{ac} = \vec{0}$ makes sense (no QS systems in any strains)

1. Matrix curation/generation code
   - generate random matrices with a set sparsity
   - use matrices that represent special adjacency graphs (e.g. planar graphs)
   - find matrices inspired by actual bacterial systems
     - @hiller_2020 may be a good starting point

1. Simulate how this model works on microbiome data
   - use real moicrobiome (OTU tables) data as initial conditions
   - get OTU tables labeled with disease states (i.e. has IBD/ doesnt have IBD)
   - quantify distance of the terminal state from the model (abundance vector) to a known disease state
   - possible starting points
     - [Git repo with several microbiome datasets](https://github.com/twbattaglia/MicrobeDS)
     - [HMP search result](https://portal.hmpdacc.org/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22sample.study_name%22,%22value%22:%5B%22IBDMDB%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22file.format%22,%22value%22:%5B%22Biological%20Observation%20Matrix%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22file.matrix_type%22,%22value%22:%5B%2216s_community%22%5D%7D%7D%5D%7D&pagination=%7B%22files%22:%7B%22count%22:20,%22total%22:23911,%22page%22:1,%22pages%22:1196,%22from%22:0,%22sort%22:%22file.format:desc,%22,%22size%22:20,%22sample_total%22:2375%7D%7D&facetTab=files)

1. Start writing the background, biological motivation for the final report and intro slides
   - what are QS systems?
   - what makes QS systems incompatible and how does this lead to "cheating"?
   - are there medical/research/environmental reasons to care about this?
   - steal the cool diagram from @eldar_2011

## Useful Links

- [link to pandoc docs on slideshows](https://pandoc.org/MANUAL.html#slide-shows)
  - notes on formatting and stuff, generally good reference
- [link to pandoc docs on citations](https://pandoc.org/MANUAL.html#citation-syntax)
  - you can just follow the examples in the report/slides templates
- [link on writing reports with pandoc](https://opensource.com/article/18/9/pandoc-research-paper)
  - useful notes on referencing sections/figures in text

# Bibliography

