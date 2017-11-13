all: slides-less_basic

slides-%:
	pandoc -t beamer -s $*.md -o $*.pdf
