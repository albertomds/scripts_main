# Tutorial Template

Use this structure when adding new tutorials to `CODEX_allScripts`.

## Goal

Briefly explain what the tutorial does.

## When to use this script

Explain the intended use case and the type of project where this script is
appropriate.

## Requirements

List required software, Python packages, external tools, and local data files.

## Folder structure

Show the relevant files:

```text
tutorial_name/
├── README.md
├── run_example.py
├── inputs/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Input files

Explain expected inputs and where users should place them. Do not commit large
molecular files, trajectories, binary files, or unpublished research data.

## How to run

Give the command:

```bash
python run_example.py
```

## Main script

Point to the script location under `scripts/`.

## Expected output

Explain printed results, output files, logs, and any plots or tables.

## How to adapt

List variables and paths that users should edit before running real work.

## Troubleshooting

List common problems, such as missing dependencies, input path errors, or
version-specific API changes.

## Citation

Explain what software, methods, force fields, datasets, and publications should
be cited.

## Next steps

Suggest the tutorial that should come next.
