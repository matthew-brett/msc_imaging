all: slides-less_basic

slides-%:
	pandoc -t beamer -s $*.md -o $*.pdf

assessment:
	pandoc -s assessment_b_full.md -o assessment_b_full.pdf
