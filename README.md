# newsletter

Monthly AstroPAH Newsletter building pipeline with Github actions and pandoc

## Pipeline notes

### A high level overview

1. Each abstract entry for the month are written in independent YAML files, looking something like this:
```yaml
authors: Herzberg, G. H.; Hougen, J.; Watson, J.    # Author names MUST BE SEPARATED WITH ;, however can be in any order!
journal: The Journal of Chemical Physics
doi: 10.215.613/216.671717                          # optional field
abstract: All the cool stuff in this paper
```
2. The In Focus and Editorials will be written in [Markdown](https://www.markdownguide.org/basic-syntax/). This means that both editors _and_ contributors need to focus on content only, and we can make final adjustments on Overleaf.
3. A new issue can be triggered by making a pull request, with a message `/timetoscience`.

### Workflow and running the pipeline

1. `issue_details.md` contain a YAML header that sets some information used for the current issue. You can also use it to control which sections are built, for some issues where not every section is populated. Double check these values every issue, including updating the issue number.
2. Overwrite the `cover.png` in the `cover/` folder to replace the image. Update details accordingly in `issue_details.md`.
