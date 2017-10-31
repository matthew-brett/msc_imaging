all: slides-basic

slides-%:
	pandoc -t beamer -s $*.md -o $*.pdf
