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


title: How Quorum Sensing Interactions Affect Microbial Population Structure
subtitle: 02712 Final Project
author: Sid, Neel, Sarah, Deepika, Evan
date: \today
institute: Carnegie Mellon University
---

# Background

## Quorum-Sensing Systems

## Public Goods and Cheating

## Maintaining Freeloaders as a Diversity Reservoir

## Signal-Receptor Activation Matrix $K_{ac}$

- Represents all receptors-signal pairs ($R_iS_i$) present in at least 1 OTU
- $K_{ac}$ is of dimension $|R|\times|S|=|N|\times|N|$
- Different sets of receptor-signal combinations can produce the same $K_{ac}$

---

\onslide<1->
### Facultative Cheaters 
Matrix for 2 strains $R_1S_1$ and $R_2S_2$ $\qquad\qquad\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\hfill$

\onslide<2->
### Obligate Cheater
Matrix for 2 strains $R_1S_1$ and $R_0S_0$ \qquad\qquad$\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\hfill$

\onslide<3->
### Custom Matrix
Matrix for 2 strains $R_1R_2S_1$ and $R_2S_2$ $\qquad\quad\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\hfill$

# Model

# Results

# Example Section 

## Citation Example
- the citation file is at `./Documents/citations.bib`
  - bibtex foramtted file
  - zotero/mendel/citation websites can produce this format automatically for papers
- here is the syntax `@eldar_2011`
  - `eldar_2011` is the cite key in the citation file
- here is a citation of the main paper @eldar_2011
- here is a citation of the main paper [@eldar_2011]

## Example 2 column slide
:::: {.columns}
::: {.column width="50%"}
![HGT Mechanisms](hgt_mechanisims_trendslgt.png){height=200}
:::
::: {.column width="50%"}
- **Transformation:** Incorporation of free-floating DNA into the genome
- **Conjugation:** Transfer of DNA through cell-cell connections
- **Transduction:** Transfer of DNA via phage
:::
::::

## table with math
\begin{table}
    \centering
    $\begin{array}{llll}
    \toprule
    Genotype & \multicolumn{3}{c}{Environment} \\
    \cmidrule(r){2-4}
        & E_n & E_b & E_a \\
    \midrule
    RCH & 1-2s_m & (1+s_p)(1-2s_m) & (1+s_p)(1-2s_m) \\
    RCh & 1- s_m & (1+s_p)(1- s_m) & (1+s_p)(1- s_m) \\
    RcH & 1- s_m & 1- s_m          & (1+s_p)(1- s_m) \\
    Rch & 1      & 1               & 1+s_p           \\
    rCH & 1-2s_m & (1+s_p)(1-2s_m) & 1-2s_m          \\
    rCh & 1 -s_m & (1+s_p)(1- s_m) & 1-s_m           \\
    rcH & 1- s_m & 1- s_m          & 1-s_m           \\
    rch & 1      & 1               & 1               \\
    \bottomrule
    \end{array}$
    \caption{Relative fitness values for each genotype in each environment}
    \label{ft}
\end{table}

## Math and Numbered List
- $g$ represents each genotype
1. **Gene Transfer:** $x_g^t = x_g + \sum_{x_R} x_{\neg g}x_R h(x_{\neg g},x_R)$
   - if $g=RCH$ then $\neg g=rCH$, same for $CH,cH,Ch,ch$
   - defined for R genotypes ($x_R$), for r genotypes subtract the sum
   - $h()$ probability of transfer, increases for each $H$ allele ($g_h,g_H,2g_H$)
1. **Mutation:** $x_g^s = (1-\mu(g))x_g^t + \mu(g)x_{\neg g}^t$
   - $\mu(g)$ is $\mu_{r\to R}$ for r genotypes and$\mu_{R\to r}$ for R genotypes
1. **Selection:** $x_g' = \frac{x_g^sf(g)}{\bar{w}}$
   - $f(g)$ picks the correct fitness modifier from Table 2
   - average fitness $\bar{w} = \sum_g x_g^sf(g)$

## Example code block

```python
def foo(bar):
    for i in range(69, 420):
        if i == 69 or i == 420:
            print('nice')
        else:
            print(bar)
    return None
```

## Bibliography {.allowframebreaks}
