---
nocite: '@*'
theme: Ilmenau
colortheme: dolphin
header-includes:
- \usepackage{booktabs}
- \setbeamercolor{block title}{bg=blue!50}
- \setbeamercolor{block body}{bg=blue!10}
- \setbeamertemplate{itemize item}{\scriptsize$\blacktriangleright$}
- \setbeamertemplate{itemize subitem}{\scriptsize$\diamond$}
- \setbeamertemplate{enumerate items}{\insertenumlabel.}
- \setbeamertemplate{section page}{\begin{centering} \usebeamerfont{section title}\insertsection\par\end{centering}}


title: How Quorum Sensing Interactions Affect Population Structure
subtitle: 02-712 Final Project
author: Sid Reed, Neel Mehtani, Sarah Wenger, Deepika Yeramosu, Evan Trop
date: \today
institute: Computational Biology Department, Carnegie Mellon University
---

# Background

## Quorum-Sensing Systems

:::: {.columns}
::: {.column width="55%"}
![ @qs_diagram](qs_diagram.png){width=\textwidth}
:::
::: {.column width="50%"}
- Signal-Receptor molecule pairs that modulate gene expression

- Once threshold density is reached, enough signal is received to upregulated target genes

- Can lead to biofilms, antibiotic production etc.
:::
::::

## Public Goods and Cheating

:::: {.columns}
::: {.column width="55%"}
![ @eldar_2011](eldar_2011_fig1.png){width=\textwidth}
:::
::: {.column width="50%"}
- When quorum is reached, bacteria produce a "public good"

- Everyone benefits from this even if they don't contribute

- Must produce the receptor, signal molecule and good to contribute

- Cheaters DO prosper (if you are a bacterium)

:::
::::

## Who Cares?

- check the discussion from @eldar_2011 for references

\onslide<1->
### Maintaining Freeloaders as a Diversity Reservoir

\onslide<2->
### Kin Recognition for Strains

\onslide<3->
### Designing Cheaters to Disrupt Pathogen Growth

# Model

## Signal-Receptor Activation Matrix $K_{ac}$

- Represents all receptors-signal pairs ($R_iS_i$) present in at least 1 OTU in the population
- Different sets of receptor-signal combinations can produce the same $K_{ac}$
- $K_{ac}$ is of dimension $|R|\times|S|=|N|\times|N|$

---

\onslide<1->
### Facultative Cheaters 
Matrix for 2 strains $R_1S_1$ and $R_2S_2$ $\qquad\qquad\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\hfill$

\onslide<2->
### Obligate Cheater
Matrix for 2 strains $R_1S_1$ and $R_0S_0$ \qquad\qquad$\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\hfill$

\onslide<3->
### Custom Matrix
Matrix for 2 strains $R_1R_2S_1$ and $R_2S_2$ $\qquad\quad\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$\
or 3 strains $R_1S_1$, $R_2S_1$ and $R_2S_2$

# Results

## Comparing Different K_ac Matrices

\vspace{1em}
![](k_ac_comparisons.png)

## How K_ac Sparsity Affects Model Dynamics

## Using Gut Microbiome Data

## Bibliography {.allowframebreaks}
