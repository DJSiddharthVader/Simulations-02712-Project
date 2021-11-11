02712 Final Project
===================

# How Quorum Sensing Interactions Affect Microbial Population Structures

__Authors:__ Sid, Neel, Evan, Sarah, Deepika

## TODO

- [ ] We implement the model described in @eldar_2011
  - [ ] ideally we use actual python ODE solvers for efficiency/accuracy reasons
  - [ ] stopping conditions is either set time limit or reaching a stationary distribution
  - [ ] develop a "null" model to compare against
    - [ ] I think $K_{ac} = \vec{0}$ makes sense (no QS systems in any strains)

- [ ] Write code to analyze simulations results
   - [ ] total population growth rate
   - [ ] time until at stationary distribution
   - [ ] "difference" between terminal/initial state
     - population diversity at terminal state
       - [ ] alpha/beta diversity
       - [ ] Bray-Curtis distance
   - [ ] total populations size
   - [ ] number of species that go extinct/ how quickly

- [ ] Matrix curation/generation code
  - [ ] generate random matrices with a set sparsity
  - [ ] use matrices that represent special adjacency graphs (e.g. planar graphs)
  - [ ] find matrices inspired by actual bacterial systems
    - @hiller_2020 may be a good starting point

- [ ] Simulate how this model works on microbiome data
  - [ ] quantify distance of the terminal state from the model (abundance vector) to a known disease state
  - [ ] get OTU tables labeled with disease states (i.e. has IBD/ doesnt have IBD)
    - [Git repo with several microbiome datasets](https://github.com/twbattaglia/MicrobeDS)
    - [HMP search result](https://portal.hmpdacc.org/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22sample.study_name%22,%22value%22:%5B%22IBDMDB%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22file.format%22,%22value%22:%5B%22Biological%20Observation%20Matrix%22%5D%7D%7D,%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22file.matrix_type%22,%22value%22:%5B%2216s_community%22%5D%7D%7D%5D%7D&pagination=%7B%22files%22:%7B%22count%22:20,%22total%22:23911,%22page%22:1,%22pages%22:1196,%22from%22:0,%22sort%22:%22file.format:desc,%22,%22size%22:20,%22sample_total%22:2375%7D%7D&facetTab=files)

- [ ] Start writing the background, biological motivation for the final report and intro slides
  - [ ] what are QS systems?
  - [ ] what makes QS systems incompatible and how does this lead to "cheating"?
  - [ ] are there medical/research/environmental reasons to care about this?
  - [ ] steal the cool diagram from @eldar_2011 (Fig 2?)

## Compiling Documents

Requires:
  - `GNU make`
  - `pandoc`

I created a Makefile for running the pandoc commands to compile the documents more easily.
You can compile the documents with the Makefile as follows

```bash
$ make outline   # make the outline ./Documents/published/outline.pdf
$ make slides    # make the slides ./Documents/published/slides.pdf
$ make report    # make the final report ./Documents/published/report.pdf
$ make documents # all of the above
$ make publish   # run documents and git push everything
```

## Running the Code

## Replicating results

