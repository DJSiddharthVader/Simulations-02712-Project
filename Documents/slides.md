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
author: Sid Reed, Evan Trop, Neel Mehtani, Deepika Yeramosu, Sarah Wenger
date: \today
institute: Carnegie Mellon University
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

- QS pattern can be shaped by evolution, interesting case study
- Divegent QS systems can help maintain kin diversity
- Analysis of QS systems can help inform strategies for resisting pathogenesis
  - interfere with mircobiome colonization
  - interfere with biofilm formation and competitions

# Methods

## Basic ODE Model

\centering
![](eldar_title.png){width=300}

\onslide<2->
### Model Equations
\begin{align*}
    \frac{dn_i}{dt} &= n_i(\frac{P_d}{P_d+1}(1-rf(R^{active}_i))-n_{tot}-\gamma_n)\\
    \frac{dS_i}{dt} &= \beta_S(n_i-S_i)\\
    \frac{dE}{dt} &= -\beta_EE+\sum_i f(R^{active}_i)n_i\\
    \frac{dP_d}{dt} &= J_{P_d}+V_{max}E-\beta_{P_d}(\frac{P_d}{P_d+1})n_{tot}
\end{align*}

## Signal-Receptor Activation Matrix $K_{ac}$

- The interaction term is defined as $R^{active} = \frac{K_{ac}\vec{S}}{K_{RS}+K_{ac}\vec{S}}$
  - assumes Michalis-Menten dynamics of signal-receptor binding ($K_{RS}$ is a constant)

- $K_{ac}$ represents all receptors-signal pairs ($R_iS_i$) produced in each strain

- $K_{ac}$ is of dimension $|R|\times|S|=|n|\times|n|$

---

\onslide<1->
### Facultative Cheaters 
Matrix for 2 strains $R_1S_1$ and $R_2S_2$ $\qquad\qquad\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\hfill$

\onslide<2->
### Obligate Cheater
Matrix for 2 strains $R_1S_1$ and $R_0S_0$ \qquad\qquad$\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\hfill$

\onslide<3->
### Custom Matrix
Matrix for 2 strains $R_1S_2S_1$ and $R_2S_2$ $\qquad\quad\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$\

## Our Work

- Implemented in python using `scipy.integrate.solve_ivp` 
- Generated different $K_{ac}$ matrices and run simulations
  - Specific patterns and randomly generated $K_{ac}$
- Examine population structure and model dynamics 
- Simulate using gut microbiome data as initial state
- All code/results easily available to use on Github

# Results

## Comparing Different $K_{ac}$ Matrices

\vspace{0.25em}
![](k_ac_comparisons.png)

## How Different $K_{ac}$ affect model dynamics

:::: {.columns}
::: {.column width="55%"}
![](fixation_time_comparison.png)
:::
::: {.column width="55%"}
![](shannon_index_comparison.png)
:::
::::

## How $K_{ac}$ Sparsity Affects Population Structure

![](sparsity_analysis.png){width=425}

## Discussion

### Findings

- Patterns and sparsity can have large effects on population trajectories
- Not a linear relationship between sparsity and total growth rate
  - cheating does not always benefit everyone
- Different $K_{ac}$ have strong effects on population diversity

\onslide<5->
### Extensions

- Generalize $K_{ac}$ 
- Simulating with real microbiome data
- Using biologically informed $K_{ac}$ (@hiller_2020)
- Fit this framework onto other biological systems
  - modelling fish Tinder

## Moral of the Study

\begin{center}
\onslide<2->{\Huge Cheating works...}\\
\vspace{0.1em}
\onslide<3->{\tiny(for bacteria)}\\
\onslide<4->{\Huge but cooperating is better!}\\
\end{center}

## Bibliography {.allowframebreaks}
