---
nocite: '@*'
theme: Dresden
header-includes:
- \usepackage{booktabs}

title: "Project: Biological Modeling & Simulations 02-712"
subtitle: How Quorum Sensing Interactions Affect Microbial Population Structures
author: Sid, Neel, Sarah, Deepika, Evan
date: \today
institute: Carnegie Mellon University
---

# Example Section Title 1

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

## Math and sub lists
- Haploid population
- infinite population
- Each generation we have 1) gene transfer 2) mutation and 3) selection
  - no sexual reproduction, consider gene transfer step
  - Gene transfer is  analogous to oblique learning from Fogarty L. 2018
  - mutation is $r \to R$ or $R \to r$

# Example Section Title 2

## Example Table
\begin{table}
    \centering
    \begin{tabular}{@{}lll@{}}
        \toprule
        \multicolumn{2}{c}{Allele} & Description \\
        \cmidrule(l){1-2}
        Major & Minor & \\
        \midrule
        $R$ & $r$ & has/does not have resistance gene \\
        $H$ & $h$ & HGT machinery is expressed/not expressed  \\
        $C$ & $c$ & CRISPR-Cas is expressed/not expressed \\
        \bottomrule
    \end{tabular}
    \caption{Allele definitions}
\end{table}


## More complicated table with math
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

## Lots of math
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

## slide with subsections

### Slide subsection 1
- resistance allele dominates even outside of antibiotic pressure
- environmental turnover rate significantly affects genotype frequencies

### Slide subsection 2
  - explore parameter space and look for empirical justifications
  - model phage population dynamics directly
  - incorporate terms that reflect biological trade-off of HGT/CRISPR

## Bibliography {.allowframebreaks}
