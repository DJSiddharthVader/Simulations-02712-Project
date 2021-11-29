---
documentclass: article
classoption: twocolumn
geometry: margin=1in
fontsize: 12pt
nocite: '@*'
linkcolor: blue
header-includes:
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
    affiliation: 1,2
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
  - num: 2
    name: Department of Being Sick, Cool University
abstract: "example abstract"
---

*[OTU]: Operational Taxonomic Unit

# Background

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

### How Sparsity affects model dynamics

### Examining well-known adjacency matrices

## Simulations with OTU data
The data we use is an OTU table $O_I$, an $m\times n$ matrix representing the abundance of $m$ OTUs across $n$ samples.
For each sample we use the abundance vector as our initial state and run the simulation with a given set of parameters.
So after all simulations we get an OTU table $O_T$ representing the terminal state of the model (abundance vector) for each initial state.
Given the tables $O_I, O_T$ for each sample we can calculate 

- difference in $\alpha$-diversity (richness and Shannon Index)
- $\beta$-diversity (Bray-Curtis distance)
- difference in skewness (Fisher's Coefficient of skewness)
- total population growth rate 

and we examine how these statistics vary when using different $K_a$ matrices and the same $O_I$.

## Simulation with an empirically derived QS interaction matrix

# Discussion

# Bibliography
