# newsletter

Monthly AstroPAH Newsletter building pipeline with Github actions and pandoc

## Pipeline notes

### A high level overview

1. Each abstract entry for the month are written in independent YAML files, looking something like this:
```yaml
authors: Herzberg, G. H.; Hougen, J.; Watson, J.
journal: The Journal of Chemical Physics
doi: 10.215.613/216.671717                      # optional field
abstract: All the cool stuff in this paper
```
2. The In Focus and Editorials will be written in [Markdown](https://www.markdownguide.org/basic-syntax/). This means that both editors _and_ contributors need to focus on content only, and we can make final adjustments on Overleaf.
3. A new issue can be triggered by making a pull request, with a message `/timetoscience`.

### Workflow and running the pipeline

Plan is to use github actions with `pandoc` to build the issue Markdown and YAML files. Abstracts can be stored as YAML as they're structured data that contain more or less the same amount of information for each abstract. The Editorial and the In Focus will be Markdown, where editors/contributors will simply type their pieces in plain Markdown.

We'll implement a Python script that will combine the Markdown/YAML into a single Markdown file in one Github action. A second action will then trigger on success to run `pandoc` to build the TeX and LaTeX files. 

### Starting a new issue

Use a [rebase action](https://github.com/cirrus-actions/rebase) via a PR to force a rebase of a "template" branch onto `main`.
