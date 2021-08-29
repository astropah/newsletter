tex:
	pandoc issue_details.md -o issue.tex --template template.tex

pdf:
	latexmk -f -interaction=nonstopmode issue.tex

clean:
	latexmk -c

all: 
	tex pdf clean
