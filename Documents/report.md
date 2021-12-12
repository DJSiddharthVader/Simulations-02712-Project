---
documentclass: article
geometry: margin=1in
fontsize: 12pt
nocite: '@*'
linkcolor: blue
header-includes:
  - \usepackage{float}
  - \usepackage{placeins}
  - \usepackage{setspace}
  - \usepackage{amsfonts}
  - \usepackage{tikz-network}
  - \usepackage{blkarray}
  - \usepackage{booktabs}

title: How Quorum Sensing Interactions Affect Population Structures
subtitle: "02-712 Final Project"
date: \today
author:
  - name: Siddharth Reed
    affiliation: 1
    email: slreed@andrew.cmu.edu
  - name: Evan Trop
    affiliation: 1
  - name: Neel Mehtani
    affiliation: 1
  - name: Deepika Yeramos
    affiliation: 1
  - name: Sarah Wenger
    affiliation: 1
institute:
  - num: 1
    name: Computational Biology Department, Carnegie Mellon University
abstract: "example abstract"
---

\newpage

# Background

Quorum sensing (QS) involves the ability of bacteria to change their population behavior. QS systems consist of a signal molecule that is constitutively expressed and a complementary receptor. When the population density of the bacteria reaches a certain threshold, the increased concentration signal bound receptor triggers expression of a public good such as a biofilm, surfactin, or enzyme to break down a complex nutrient.

These QS systems resemble some form of kin recognition as only bacteria that produce the unique signal - receptor pair take part in the production of the public good. However, bacteria that do not produce the signal - receptor pair, also called “cheaters”, can take advantage of the public good without incurring the expense of signal or public good production. Cheaters help maintain diversity in QS signaling systems as diverged incompatible QS systems are still maintained at the population level through the indiscriminate public good [@pollak_2015].

These QS interactions naturally give rise to a matrix where row r_i represents straini’s receptor and column si represents straini’s signal. Matrix values are one if receptor - signal binding is possible and zero otherwise. Our project aims to understand how QS interactions amongst different bacterial strains affect the population structure. Specifically, we are interested in answering how different biologically relevant matrix patterns and matrix sparsity affect population statistics such as total population growth rate, population diversity, time until fixation. Developing an understanding of the significance of these QS interactions might allow one to manipulate microbial environments. This could prove to be a useful tool in medical applications such as gastrointestinal diseases or in improving environmental states in wastewater treatment facilities.

Previous studies of QS systems have explored how and why evolutionary divergence of QS pathways occurs as well as how population diversity is maintained in the presence of obligate cheaters. These studies do not  investigate how specific patterns and level of interactions between QS systems affect population structure.


# Methods

## Basic QS Interaction Model

### Assumptions
- Very basic assumption is that QS directly controls the levels the public good production
- Signal production is constitutive and quorum response is density dependent function of signal-bound receptor
- QS system is composed of 3 genes encoding signaling molecule ($S$), receptor molecule ($R$), and public good product
- The public good is a secreted enzyme whose product is a usable nutrient
- Growth rate is dependent on the level of usable nutrient, Hollings type II term
- Producing the public good reduces growth rate
- Density dependent cell death, leading to a logistic form of growth equation
- In the two divergent allele model (R1,R2) and (S1,S2), only 1 mutation allows the transition between alleles. R1 can only bind S1 and R2 can only bind S2
- The public good is an Exo-enzyme ($E$), that  catalyzes the cleavage of a complex nutrient ($P$) into a transportable form ($P_d$)
  - Level of $P$ is constant  
- A fraction $r$ of the growth potential is diverted from growth to enzyme production at max production level
- Quorum response function is a monotonically increasing function with maximum of 1
- $R$-$S$ interaction occurs on a much faster time scale so they are in a quasi steady state and levels of receptor is constant --> Michaelis Menton Relationship between $[RS]$ and $S$
- Quorum response form is $f(x) = x^m$

# Results

## Comparing QS interaction matrices

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/k_ac_comparisons.png}
\caption{}
\label{comparison}
\end{figure*}
\FloatBarrier

Text about matrices

## Examining specific adjacency matrices

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/pattern_analysis.png}
\label{patterns}
\caption{test}
\end{figure*}
\FloatBarrier

Text about patterns

## How sparsity affects model dynamics

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/sparsity_analysis.png}
\caption{test}
\label{sparsity}
\end{figure*}
\FloatBarrier

Text about sparsity

## Simulations with OTU data
As a way to explore our model with real data, we used data and metadata from the Inflammatory Bowel Multiomics Database to seed our simulator. The specific data we used contained taxonomic profiles for participants who were diagnosed into three classes, non-irritable bowel disease (non-IBD), ulcerative colitis(UC), and crohn's disease(CD).

We were interested in observing if different biologically relevant interaction matrix patterns ($K_ac$) would play a role in differentiating the different disease states. For each set of participants with the same diagnosis, we created a strain abundance list which consisted of every bacterial strain and its corresponding average abundance derived from the taxonomic profiles of the participants.
Simulations were then performed for each interaction matrix pattern with the initial cell density parameter set as the normalized strain abundance list for each diagnosis. Although there is a loss of information pertaining to the growth dynamics of each strain over time, graphs corresponding to the total cell densities over time were generated for each matrix pattern.

The results below show that for most matrix patterns, given enough time, total cell densities are very similar across all diagnosis types. We observe differentiation between non-IBD and disease states for the case where all strains have the same receptor and are considered naive cooperators. Differentiation in the trajectory of total cell density is also observed for the identity matrix pattern which signifies that each bacteria has an independent qs system. An interesting result is that the complete matrix pattern, where every strain’s receptor binds every other strain’s signal, shows different trajectory between CD and the UC/nonIBD cases.


\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/microbiome_analysis.png}
\caption{test}
\label{microbiome}
\end{figure*}
\FloatBarrier

# Discussion

It is hard to determine whether the specific type of interaction matrix from our set of biologically relevant matrices can significantly differentiate the trajectory of total cell densities between the microbiome environments of IBD vs non-IBD. It would be interesting to use empirical interaction matrices for simulations as it could provide more insight into if these interaction matrices are important in determining disease states.

# Contributions

# Bibliography

