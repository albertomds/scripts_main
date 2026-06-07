# QC Energy Placeholder

## Goal

Provide a clean placeholder for a pDynamo3 quantum chemistry single-point energy
tutorial.

## When to use this script

Use this script after a small molecular system can be loaded and you want to
document QC model settings, charge, multiplicity, and atom selections before
running a real energy calculation.

## Requirements

- Python 3.
- A local pDynamo3 installation for real calculations.
- Local molecular input files.
- Any QC backend or optional pDynamo3 components required by the chosen model.

## Folder structure

```text
scripts/pDynamo3/02_qc_energy_placeholder/
├── README.md
├── run_example.py
├── inputs/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Input files

Place local molecular files in `inputs/`. Do not commit large structures,
trajectories, binary files, or unpublished research data.

## How to run

From `scripts/pDynamo3/02_qc_energy_placeholder/`:

```bash
python run_example.py
```

## Main script

The main script is
`scripts/pDynamo3/02_qc_energy_placeholder/run_example.py`.

## Expected output

The script prints placeholder QC settings and writes
`outputs/qc_energy_template_summary.txt`.

## How to adapt

Edit `QC_MODEL`, `TOTAL_CHARGE`, `MULTIPLICITY`, `QC_SELECTION`, and input file
paths. Then add the pDynamo3 calls needed to load the system, define the QC
region, assign the model, and evaluate the energy.

## Troubleshooting

- If pDynamo3 imports fail, verify your installation and Python path.
- If a QC model is unavailable, check optional dependencies and compiled
  components.
- If atom selection fails, inspect residue and atom names in your local input
  files.

## Citation

For real calculations, cite pDynamo3, the selected QC method, any basis set or
semiempirical model, molecular mechanics force fields, and supporting tools.

## Next steps

Add an energy analysis, geometry optimization, or QM/MM setup tutorial after the
placeholder has been adapted and tested locally.
