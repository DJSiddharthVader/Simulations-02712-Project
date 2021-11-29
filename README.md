02712 Final Project
===================

# How Quorum Sensing Interactions Affect Microbial Population Structures

__Authors:__ Sid, Neel, Evan, Sarah, Deepika

## TODO

- [x] We implement the model described in @eldar_2011
  - [x] ideally we use actual python ODE solvers for efficiency/accuracy reasons
  - [x] stopping conditions is either set time limit 

- [ ] Write code to analyze simulations results
   - [ ] figure out simulations to run and analyze
     - which matrices
     - which initial conditions 
     - how long?
     - figure out what is space/time efficient to do
   - [ ] produce a dataframe of stats from a simulation runs
     - [ ] ...
   - [ ] Code for generating results and plots
     - [ ] ...
   - [x] statistics to calculate
     - [x] population growth rate
     - [x] "difference" between terminal/initial state
       - [x] skewness of the abundance vector
       - [x] alpha diversity
         - [x] species richness
         - [x] Shannon index
       - [x] beta diversity
         - [x] Bray-Curtis distance

- [ ] Matrix curation/generation code
  - [x] develop a "null" model to compare against
    - I think $K_{ac} = \vec{0}$ makes sense (no QS systems in any strains)
  - [x] generate random matrices with a set sparsity
  - [x] use matrices that represent interesting graph patterns
  - [ ] find matrices inspired by actual bacterial systems
    - @hiller_2020 may be a good starting point

- [ ] Simulate how this model works on microbiome data
  - [x] Data and metadata from [IDBMDB](https://ibdmdb.org/tunnel/public/summary.html), OTU tables for IBD patients. (in `./Data/`)
    - specifically use the 16S data from HMP2 and the sample metadata
    - `./Data/taxonomic_profiles.tsv` is the OTU table
    - `./Data/hmp2_metadata.tsv` is the raw sample metadata
    - every sample has an ID corresponding to a column in the abundance table
  - [x] clean metadata for easy use
    - use the `./src/clean_metadata.py` script to clean the metadata
    - produces the file `./Data/filtered_hmp2_metadata.tsv` 
    - there is a `diagnosis` column with the IBD status of the patient
  - [ ] adapt model to take in this OTU data (should be easy)

- [ ] Start writing the background, biological motivation for the final report and intro slides
  - [x] what are QS systems?
  - [x] what makes QS systems incompatible and how does this lead to "cheating"?
  - [ ] are there medical/research/environmental reasons to care about this?
  - [x] steal the cool diagram from @eldar_2011 (Fig 2?)

- [ ] Include plots and figures in presentation and paper
  - [ ] heatmap of k_ac matrix (methods, also results for comparison with next plot)
  - [ ] time vs. strain abundance for different sparsity (results)
  - [ ] time vs. model dynamics (strain abundances), line plot (results)
  - [ ] time vs. model properties (alpha/beta diversity, growth rate, etc.) (results)
    - try making all of these plots, use ones that give interesting results
    - can also try to plot multiple lines on one graph (i.e. time vs. multiple model properties, time vs. one property but for diff. sparsities, etc.)
  - [ ] distributions of growth rates for a matrix (can do several matrices)

## Running the Code

### Requirements

Requires:
  - `GNU make`
  - `pandoc`
  - `python >= 3.7`
    - Use conda and the provided `environment.yml` for dependencies
    - `$ conda env create -f environment.yml`

I have provided a `Makefile` for to help replicate our results and produce documents, the specific commands to use are detailed below.

### Using the Model

If you want to run your own simulation using this model you can do the following

```bash
$ conda activate proj_02712
$ python src/model.py temp arguments idk fill in later
```

### Replicating our Results

### Compiling Documents

You can compile the documents using the Makefile as follows

```bash
$ make outline   # make the outline ./Published/outline.pdf
$ make slides    # make the slides ./Published/slides.pdf
$ make report    # make the final report ./Published/report.pdf
$ make documents # make report and slides
$ make publish   # run documents and git push them 
```

