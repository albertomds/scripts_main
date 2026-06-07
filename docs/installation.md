# Installation

This repository is intentionally lightweight. Most pages are static Markdown,
and scripts are plain Python files.

## Basic setup

Clone the repository and create a Python environment if you plan to run scripts:

```bash
git clone <repository-url>
cd CODEX_allScripts
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is currently minimal. Individual tutorial folders may list
additional software requirements.

## pDynamo3

pDynamo3 is not installed by this repository. Install and configure pDynamo3
according to your local platform and the official pDynamo3 instructions.

The pDynamo3 examples here are templates. They may need edits to import paths,
environment variables, input file names, force-field locations, and model
settings before they can run real calculations.
