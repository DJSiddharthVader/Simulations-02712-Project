02712 Final Project
===================

# How Quorum Sensing Interactions Affect Microbial Population Structures

## TODO

- [x] We implement the model described in @eldar_2011
  - [x] ideally we use actual python ODE solvers for efficiency/accuracy reasons
  - [x] stopping conditions is set end time

- [ ] Write code to compute statistics
   - [x] wrappers to compute stats on simulation results
   - [x] statistics to calculate
     - [x] population growth rate
     - [x] "difference" between terminal/initial state
       - [x] skewness of the abundance vector
       - [x] alpha diversity
         - [x] species where N_i(tn) > N_i(t0)
         - [x] Shannon index
       - [x] beta diversity
         - [x] Bray-Curtis distance

- [ ] Use model to answer Questions
  - [ ] What happens as sparsity decreases?
  - [ ] How do specific "patterned matrices affect the population?
  - [ ] What happens using real data as initial conditions?

- [ ] Writing the background, motivation and methods
  - [x] what are QS systems?
  - [x] what makes QS systems incompatible and how does this lead to "cheating"?
  - [ ] are there medical/research/environmental reasons to care about this?
  - [x] steal the cool diagram from @eldar_2011 (Fig 2?)
  - [ ] basics of the ODE model
  - [ ] one slide on Runge-Katta methods? (what scipy uses)

- [ ] Matrix curation/generation code
  - [x] develop a "null" model to compare against
    - K_ac matrix with all 0s (no signals, no receptors)
  - [x] generate random matrices with a set sparsity
  - [x] use matrices that represent interesting graph patterns
  - [ ] find matrices inspired by actual bacterial systems
    - @hiller_2020 may be a good starting point

- [x] Get microbiome data to try and simulate one
  - [x] Data and metadata from [IDBMDB](https://ibdmdb.org/tunnel/public/summary.html), OTU tables for IBD patients. (in `./Data/`)
    - specifically use the 16S data from HMP2 and the sample metadata
    - `./Data/taxonomic_profiles.tsv` is the OTU table
    - `./Data/hmp2_metadata.tsv` is the raw sample metadata
    - every sample has an ID corresponding to a column in the abundance table
  - [x] clean metadata for easy use
    - use the `./src/clean_metadata.py` script to clean the metadata
    - produces the file `./Data/filtered_hmp2_metadata.tsv` 
    - there is a `diagnosis` column with the IBD status of the patient

## Running the Code

### Requirements

Requires:
  - `GNU make`
  - `pandoc`
  - `python >= 3.7`
  - Use conda and the provided `environment.yml` for dependencies

```bash
# create and activate the conda environment
$ conda env create -f environment.yml
$ conda activate proj_02712
```

### Replicating our Results

The parameters values used for the ODE are taken from @eldar_2011 (methods section) and seen in `./src/model.py`.
All of the figures presented in our slides and report are generated with the code provided in `./src/` with all the parameters for each simulation/result in the corresponding jupyter notebook in the `./Notebooks` folder.
You can run whichever notebook to recreate the figures and tweak the parameters to see how the model behaves.

### Compiling Documents

You can compile the documents using the provided `Makefile` as follows

```bash
$ make outline   # make the outline ./Published/outline.pdf
$ make slides    # make the slides ./Published/slides.pdf
$ make report    # make the final report ./Published/report.pdf
$ make documents # make report and slides
```

