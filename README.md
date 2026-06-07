# CODEX_allScripts

Reusable scripts and tutorial templates for computational chemistry,
molecular dynamics, QM/MM workflows, enzyme catalysis studies, and data
analysis.

The repository is intentionally minimal. It stores small, readable scripts and
static Markdown tutorials that can be published with GitHub Pages from the
`docs/` folder.

## Repository layout

- `scripts/` contains reusable scripts and runnable tutorial folders.
- `examples/` contains short example notes that mirror selected scripts.
- `docs/` contains the GitHub Pages documentation.
- `requirements.txt` lists lightweight Python dependencies when needed.

## Tutorial categories

- `pDynamo3`: template-based examples for preparing and adapting pDynamo3
  workflows. These examples do not include molecular systems, trajectories,
  binaries, or unpublished research data.

## Documentation

Start with the documentation homepage:

- [Installation](docs/installation.md)
- [General examples](docs/examples.md)
- [Tutorial template](docs/tutorial-template.md)
- [pDynamo3 tutorials](docs/pDynamo3/index.md)

## Notes

pDynamo3 examples in this repository are placeholders for local adaptation.
They may require edits depending on your pDynamo3 installation, environment
variables, available force fields, and input files.

When using pDynamo3 or related force fields and methods in real work, cite the
appropriate pDynamo3 publications and any supporting software, force-field, and
method references.
