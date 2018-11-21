all: assessment-2018

slides-%:
	pandoc -t beamer -s $*.md -o $*.pdf

assessment-2018:
	pandoc -s assessment_b_2018.md -o assessment_b_2018.pdf

assessment-2017:
	pandoc -s assessment_b_full.md -o assessment_b_full.pdf

er-files:
	rm -rf er_files
	python3 ds009_onsets.py ds000009_R2.0.3 er_files emotionalregulation
	zip -r er_files.zip er_files
	rm -rf er_files

td-files:
	rm -rf td_files
	python3 ds009_onsets.py ds000009_R2.0.3 td_files discounting
	zip -r td_files.zip td_files
	rm -rf td_files
