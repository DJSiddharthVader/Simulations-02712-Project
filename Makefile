DOC_DIR=./Documents
# common resources
BIBLIO=$(DOC_DIR)/citations.bib
TEMPLATE=$(DOC_DIR)/template.tex
FIG_DIR=$(DOC_DIR)/figures
# Flags
PFLAGS=-s --from markdown+citations --citeproc --bibliography $(BIBLIO) --resource-path $(FIG_DIR)
# document dirs
ODIR=$(DOC_DIR)/outline
SDIR=$(DOC_DIR)/presentation
RDIR=$(DOC_DIR)/report


documents: outline slides report

outline:
	@pandoc $(PFLAGS) \
			--template=$(TEMPLATE) \
			$(ODIR)/outline.md -o $(ODIR)/outline.pdf
	@echo "made $(ODIR)/outline.pdf"

slides:
	@pandoc $(PFLAGS) \
	        -t beamer -i --slide-level=2 \
			$(SDIR)/slides.md -o $(SDIR)/slides.pdf
	@echo "made $(SDIR)/slides.pdf"

report:
	@pandoc $(PFLAGS) \
	        --template=$(TEMPLATE) \
			$(RDIR)/report.md -o $(RDIR)/report.pdf
	@echo "made $(RDIR)/report.pdf"

test:
	@echo $(DOC_DIR)
	@echo $(BIBLIO)
	@echo $(TEMPLATE)
	@echo $(FIG_DIR)
	@echo $(PFLAGS)
