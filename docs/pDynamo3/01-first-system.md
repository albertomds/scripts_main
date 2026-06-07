# First pDynamo3 System

## Goal

Set up a minimal folder and script template for a first pDynamo3 system
workflow.

## When to use this script

Use this script when starting a new pDynamo3 tutorial and checking that the
local folder structure is ready before adding real molecular input files.

## Requirements

- Python 3.
- A local pDynamo3 installation for real calculations.
- User-supplied molecular input files.

## Folder structure

```text
scripts/pDynamo3/01_first_system/
├── README.md
├── run_example.py
├── inputs/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Input files

Place local input files in `inputs/`. This repository does not include
molecular structures, trajectories, binary files, or unpublished research data.

## How to run

From `scripts/pDynamo3/01_first_system/`:

```bash
python run_example.py
```

## Main script

The main script is
`scripts/pDynamo3/01_first_system/run_example.py`.

## Expected output

The template prints setup guidance and writes
`outputs/template_summary.txt`.

## How to adapt

Edit `EXPECTED_INPUT`, input paths, force-field choices, and any future pDynamo3
imports or system-loading calls. pDynamo3 APIs and environment settings may vary
between installations.

## Troubleshooting

- If pDynamo3 imports fail after adaptation, check your Python environment.
- If the script cannot find inputs, confirm files were placed under `inputs/`.
- If output writing fails, check directory permissions.

## Citation

For real calculations, cite pDynamo3 and any force fields, input preparation
tools, and methods used in the adapted workflow.

## Next steps

Adapt the QC energy placeholder once a small system can be loaded reliably.
