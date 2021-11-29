DOC_DIR=./Documents
OUT_DIR=./Published
# common resources
BIBLIO=$(DOC_DIR)/citations.bib
TEMPLATE=$(DOC_DIR)/template.tex
FIG_DIR=$(DOC_DIR)/figures
RESULTS_DIR=./Results
RESOURCES=$(RESULTS_DIR):$(FIG_DIR)
# Flags
PFLAGS=-s --from markdown+citations -citeproc --bibliography $(BIBLIO) --resource-path $(RESOURCES)

publish: documents
	@git add $(OUT_DIR)/*.pdf
	@git commit -m 'recompiled documents with makefile'
	@git push

documents: slides report

outline:
	@pandoc $(PFLAGS) \
			--template=$(TEMPLATE) \
			$(DOC_DIR)/outline.md -o $(OUT_DIR)/outline.pdf
	@echo "made $(OUT_DIR)/outline.pdf"

slides:
	@pandoc $(PFLAGS) \
	        -t beamer -i --slide-level=2 \
			$(DOC_DIR)/slides.md -o $(OUT_DIR)/slides.pdf
	@echo "made $(OUT_DIR)/slides.pdf"

report:
	@pandoc $(PFLAGS) \
	        --template=$(TEMPLATE) \
			$(DOC_DIR)/report.md -o $(OUT_DIR)/report.pdf
	@echo "made $(OUT_DIR)/report.pdf"

test:
	@echo $(DOC_DIR)
	@echo $(BIBLIO)
	@echo $(TEMPLATE)
	@echo $(PFLAGS)
