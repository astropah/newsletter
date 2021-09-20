# newsletter

Monthly AstroPAH Newsletter building pipeline with Github actions and pandoc

## Pipeline notes

### A high level overview

The majority of content is written in Markdown, with fine-tuning once the `.tex` is built with pandoc templating. TODO: link Github repository to Overleaf.
```
The InFocus and Editorials will be written in [Markdown](https://www.markdownguide.org/basic-syntax/). This means that both editors _and_ contributors need to focus on content only, and we can make final adjustments on Overleaf.

The repository has two branches: `main` and `template`. The former is used for working on the current issue, and the latter for storing a blank canvas for each issue. The `main` branch contains the full history of the newsletter, even when we "overwrite" it with the template.

Automation is done via Github actions; currently they are set to be run manually, but can be automated based on triggers and helper bots (particularly integrated with the Github Issues workflows). There are two actions implemented:

1. Create a new AstroPAH issue (i.e. tabula rasa with the template)
2. Publish an AstroPAH issue

The latter will run the publication pipeline, generating a `.tex` and a `.pdf`, with the potential to also generate an `html` and published on Github pages (see improvements section). Currently, it doesn't work end-to-end, as there is a need sometimes to edit the `.tex` to achieve certain looks and whatnot. Ideally, we link this repository to Overleaf, and we can go back to a manual workflow.

### Workflow and running the pipeline

1. Create a new Github issue, using the issue checklist template.
2. `issue_details.md` contain a YAML header that sets some information used for the current issue. You can also use it to control which sections are built, for some issues where not every section is populated. Double check these values every issue, including updating the issue number.
3. Overwrite the `cover.png` in the `cover/` folder to replace the image. Update details accordingly in `issue_details.md`.

### Possible improvements

- Use the same pandoc templating to produce HTML, which can be pushed and hosted on Github pages.
- Link to a persistent Overleaf document: means we only have one document to work off, and all the version control is done by the Github repository.
