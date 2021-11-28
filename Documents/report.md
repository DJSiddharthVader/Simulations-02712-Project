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
