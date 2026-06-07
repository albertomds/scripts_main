# First pDynamo3 System Template

## Goal

Provide a minimal starting point for organizing a first pDynamo3 system example.

## When to use this script

Use this template when you want to test folder structure, input discovery, and
basic local pDynamo3 setup before adding real molecular data.

## Requirements

- Python 3.
- A local pDynamo3 installation for real calculations.
- Local molecular input files supplied by the user.

## Folder structure

```text
01_first_system/
├── README.md
├── run_example.py
├── inputs/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Input files

Place local input files in `inputs/`. This template does not include molecular
systems, force-field files, trajectories, binaries, or research data.

## How to run

```bash
python run_example.py
```

## Main script

The main script is `scripts/pDynamo3/01_first_system/run_example.py`.

## Expected output

The script prints template guidance and writes a small text file under
`outputs/` confirming that the folder structure is ready.

## How to adapt

Edit the variables near the top of `run_example.py`, then add pDynamo3 imports
and system-building code that match your local installation and input files.

## Troubleshooting

- If pDynamo3 imports fail, check your environment and installation path.
- If inputs are missing, add local files under `inputs/`.
- If outputs cannot be written, check folder permissions.

## Citation

For real pDynamo3 calculations, cite pDynamo3 and any methods, force fields, or
parameters used in the adapted workflow.

## Next steps

After a first system loads correctly, create a QC or MM energy example.
