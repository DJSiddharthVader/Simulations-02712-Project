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

These QS interactions naturally give rise to a matrix where row $R_i$ represents strain $i$’s receptor and column $S_i$ represents strain $i$’s signal. Matrix values are one if receptor - signal binding is possible and zero otherwise. Our project aims to understand how QS interactions amongst different bacterial strains affect the population structure. Specifically, we are interested in answering how different biologically relevant matrix patterns and matrix sparsity affect population statistics such as total population growth rate, population diversity, time until fixation. Developing an understanding of the significance of these QS interactions might allow one to manipulate microbial environments. This could prove to be a useful tool in medical applications such as gastrointestinal diseases or in improving environmental states in wastewater treatment facilities.

Previous studies of QS systems have explored how and why evolutionary divergence of QS pathways occurs as well as how population diversity is maintained in the presence of obligate cheaters. These studies do not  investigate how specific patterns and level of interactions between QS systems affect population structure.


# Methods

We first note that all code, results and figures are available on GitHub [here](https://github.com/DJSiddharthVader/Simulations-02712-Project).

In order to experiment and observe how QS interactions affect population structure we first needed to first obtain a representative model of a multi strain QS system.
The model outlined in @eldar_2011 provided us with a good basis to test our questions.
This model is defined by a system of ordinary differential equations which explain how the level of cell densities, signal molecules, enzyme, and public good change with respect to time.
Note that we have have a separate equation for each strain and signaling molecule $i \in 1 \dots N$.
\begin{align*} 
    \frac{dn_i}{dt} &= n_i(\frac{P_d}{P_d+1}(1-rf(R^{active}i))-n_{tot}-\gamma_n)\\
    \frac{dS_i}{dt} &= \beta_S(n_i-S_i)\\
    \frac{dE}{dt} &= -\beta_EE+\sum_i f(R^{active}i)n_i\\
    \frac{dP_d}{dt} &= J_{P_d}+V_{max}E-\beta_{P_d}(\frac{P_d}{P_d+1})n_{tot} 
\end{align*}

To investigate how different QS interactions affect the population levels of each strain we simulate the model with a constant set of parameters (see Table \ref{tab:param}).
<!-- All of the parameter value are constant across all simulations and are specified in Table \ref{tab:param}, all also provided by @eldar_2011 . -->
To carry out simulations of a QS system given this model, parameter set, and a given $K_ac$ matrix, the `solve_ivp` function from the scipy library is used to solve the above ODE system for a specified time range (200 time steps).
The solver specifically implements the 4th order Runge Kutta approximation method as well as adaptive time steps to ensure stability and accuracy. 
Our final resulting simulator function takes as input a vector of initial cell density for x number of strains, stopping time, and the QS interaction matrix between the all strains.

Interaction matrices $K_{ac}$ are square binary matrices with dimension equal to the number of strains.
We preformed simulations with both pre-defined matrices (e.g. identity) or with randomly generated matrices (start with a 0 matrix and randomly set entries to 1 up to a specified threshold).
To see specifically how this is implemented see `src/matrix.py` in the GitHub repository for details.

\FloatBarrier
\begin{table}[h]
    \centering
    \begin{tabular}{crl}
        \toprule
        Parameter & Value & Description \\
        \midrule
$r$ &  0.5 &            growth cost of producing the public good\\
$\gamma_n$ &  0.01 &    spontaneous cell death rate\\
$\beta_S$ &  0.1 &      density dependant cell death rate\\
$\beta_E$ &  0.2 &      spontaneous enzyme degradation rate\\
$J_{P_d}$ & 0.20 &      spontaneous usable nutrient production rate\\
$V_{max}$ &  20 &       enzyme activity rate\\
$\beta_{P_D}$ &  100 &  usable nutrient consumption rate\\
$m$ &  1 &              exponent in activation function $f(x) = x^m$\\
$K_{RS}$ &  0.025 & receptor-signal binding constant\\
$K_{ac}$ & varies & receptor-signal activation matrix\\
        \bottomrule
    \end{tabular}
\caption{Parameters and values in the ODE model defined by Eldar, 2011.}
\label{tab:param}
\end{table}
\FloatBarrier

Using this basic model we examined how using different $K_{ac}$ matrices and using microbiome data to specify initial conditions would change population trajectories and the final population

## Model Statistics

Here we list out the various model statistics calculated, the specific code is in `src/analysis.py`.
Note that $t_0$ is the initial time step and $t_n$ is the final time step.

| Statistic | Description |
|:----------|:------------|
| total     | The total abundance of all strains at $t_n$ |
| growth_rate | The total groth rate of all strains |
| has_grown | The number of strains with a larger abundance at $t_n$ than at $t_0$ |
| euclidean | The euclidean distance between abundance vectors at $t_n$ and $t_0$ |
| shannon index | The absolutve value of the difference in Shannon Entropy between abundance vectors at $t_n$ and $t_0$ ($\alpha$-diversity metric) |
| bray_curtix | The Bray-Curtis distance between abundance vectors at $t_n$ and $t_0$ ($\beta$-diversity metric) |

# Results

## Comparing $K_{ac}$ Matrices

Figure \ref{comparison} illustrates the growth rates of different bacteria strains (N1 through N6) as determined by the eight different $K_{ac}$ matrices.
We see that in most cases, a larger initial abundance is associated with a larger growth rate.
This is most apparent in the cycle and complete matrix patterns. It is also evident that regardless of initial abundance, different interaction matrices largely affect population structures.

It is interesting to note between the initial and final timesteps we can get different relative abundances and largely different trajectories depending on the matrix specified.
We still see "cheating" behaviours specified by @eldar_2011 using the `ident` matrix as even though the strains start at quite different abundances the least abundant strains (6 times smaller) still end up at similar final abundances to the most abundant initial strain.
This is because the most abundant strain reaches quorum quickly, produces the public good and allows all other strains to benefit and grow without cost i.e. cheat.

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/k_ac_comparisons.png}
\caption{Population trajectories for 6 differnt strains using the ODE with different $K_{ac}$ matrices specified. The initlal abundances for each strain are $(0.0006, 0.001, 0.0015, 0.002. 0.0025, 0.003)$, chosen arbitrarily.}
\label{comparison}
\end{figure*}
\FloatBarrier

## Examining Specific $K_{ac}$ Matrices

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/pattern_analysis.png}
\label{patterns}
\caption{How different $K_{ac}$ matrices can affect how a microbial population evolves. Each line represents the empirical cumulative distribution function of each statistic. Each color represents a different $K_{ac}$ matrix.}
\end{figure*}
\FloatBarrier

test

## How $K_{ac}$ Density Affects Populations

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/sparsity_analysis.png}
\caption{Evaluation of different model statistics (columns) with different numbers of strains $N$ (rows). For each number of strains and statistics 250 simulations were run with random initial conditions. Shaded areas represent standard deviation of each statistic across the random initial conditions. Density specifically refers to $\frac{\text{sum}(K_{ac})}{|N|\times|N|}$, i.e. the fraction of all entries in $K_{ac}$ that are non-zero.}
\label{sparsity}
\end{figure*}
\FloatBarrier

For this we wanted to examine how the sparsity of the $K_{ac}$ can affect the population.
Specifically, if a system has more QS interactions (more entries equal to 1) does this affect population sizes or relative abundances over time.
In order to do so we generate $K_{ac}$ matrices randomly, starting with the null matrix (all 0s) and randomly set some entry $K_{ac}[i,j]$ to 1 and continue to set a new non-zero entry to 1 until some fraction $f$ of all entries in the matrix are filled.
So  if we have a $4\times 4$ matrix and $f=0.5$ then we will generate 8 random matrices, with $1,2,\dots,8$ entries randomly chosen to not be zero.
Note that the plots are quite jagged in some cases due to the limited size of the matrix.
For example, filling $3\times 3$ up to $f=0.5$, you can only fill 4 of 9 entries so we only get results for 4 specific sparsity values. 
This is less apparent with larger populations (i.e. larger matrices).
Again the specific function for is `random_matrix_generator()` in `src/matrix.py`.

So for each $K_{ac}$ 250 simulations with random initial conditions are run and model statistics are calculated  as shown in Figure \ref{sparsity}.
It is interesting to note that as we increase the density (number of non-zero entries) we can observe specific trends, like the Bray-Curtis distance  increasing and then plateauing at near 0.2.
We see a similar but nosier correlation between density and euclidean distance, although this may be explained by the fact that Bray-Curtis was designed specifically to compare the diversity of populations while euclidean is a generic measure of distance.
It may be that despite the increasing density ultimately less than half of all possible QS interactions are present and this results in certain populations largely growing or shrinking over the course of the simulation.
The growth rate and total abundance do not seem to obey obvious trends but this may be the result of "flattening" all of the information from each strain and looking at these statistics over all strains. 

Regardless it does appear that just the amount of QS interactions alone can strongly influence population trajectories, specifically how "different" the final population is from the original.

## Simulations with OTU data

\FloatBarrier
\begin{figure*}[h]
\centering
\includegraphics[width=\linewidth]{Documents/figures/microbiome_analysis.png}
\caption{We plot the total abundance of all strains across time for each condition. In each case we use the specified $K_{ac}$ matrix with 133 strain abundances (normalized) from a single patient with each condition.}
\label{microbiome}
\end{figure*}
\FloatBarrier

We obtained microbiome data from HMP2, including OTU (Operational Taxonomic Unit) abundance data from stool samples and patient metadata [@microbiome].
Specifically we care about the disease status as patients were either healthy (nonIBD), have ulcerative colitis (UC) or Crohn's Disease (CD).
We had abundance data from 174 samples for 982 OTUs with 44 nonIBD, 44 UC and 86 CD samples.
We use these abundance vectors as initial populations to our QS model and analyze the population trajectories. 

We were interested in observing if different biologically relevant interaction matrix patterns ($K_{ac}$) would play a role in differentiating the different disease states.
For each set of participants with the same diagnosis, we created a strain abundance list which consisted of every bacterial strain and its corresponding average abundance derived from the taxonomic profiles of the participants.
Simulations were then performed for each interaction matrix pattern with the initial cell density parameter set as the normalized strain abundance list for each diagnosis.
Although there is a loss of information pertaining to the growth dynamics of each strain over time, graphs corresponding to the total cell densities over time were generated for each matrix pattern.

The results below show that for most matrix patterns, given enough time, total cell densities are very similar across all diagnosis types.
We observe differentiation between non-IBD and disease states for the case where all strains have the same receptor and are considered naive cooperators.
Differentiation in the trajectory of total cell density is also observed for the identity matrix pattern which signifies that each bacteria has an independent QS system.
An interesting result is that the complete matrix pattern, where every strain’s receptor binds every other strain’s signal, shows different trajectory between CD and the UC/nonIBD cases.

# Discussion

It is hard to determine whether the specific type of interaction matrix from our set of biologically relevant matrices can significantly differentiate the trajectory of total cell densities between the microbiome environments of IBD vs non-IBD.
It would be interesting to use empirical interaction matrices for simulations as it could provide more insight into if these interaction matrices are important in determining disease states.

#### Contributions

| Contribution       | People
|:-------------------|:------------------------
| Building the model | Sid, Evan, Neel
| Analysis           | Sid, Evan, Neel, Deepika, Sarah
| Presentation       | Sid, Evan, Neel, Deepika, Sarah
| Writing the report | Sid, Evan, Neel, Deepika, Sarah

\newpage

# Bibliography
