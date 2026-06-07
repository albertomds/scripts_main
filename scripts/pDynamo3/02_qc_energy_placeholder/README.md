# QC Energy Placeholder Template

## Goal

Provide a placeholder layout for a pDynamo3 quantum chemistry single-point
energy tutorial.

## When to use this script

Use this template after you have a small molecular system and want to document
where QC model choices and atom selections will be added.

## Requirements

- Python 3.
- A local pDynamo3 installation for real calculations.
- Locally supplied structure files and QC method settings.

## Folder structure

```text
02_qc_energy_placeholder/
├── README.md
├── run_example.py
├── inputs/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Input files

Place local molecular input files in `inputs/`. No molecular structures or
research data are included in this template.

## How to run

```bash
python run_example.py
```

## Main script

The main script is `scripts/pDynamo3/02_qc_energy_placeholder/run_example.py`.

## Expected output

The script prints the placeholder QC settings and writes a small text summary to
`outputs/`.

## How to adapt

Edit the QC model name, charge, multiplicity, atom selection, and input file
paths near the top of `run_example.py`. Then add the pDynamo3 calls required by
your installed version.

## Troubleshooting

- If pDynamo3 modules cannot be imported, verify your Python environment.
- If a QC backend is unavailable, check optional pDynamo3 components.
- If atom selections fail, inspect residue names and atom labels in your local
  structure.

## Citation

For real calculations, cite pDynamo3 and the QC method, basis set or semiempirical
model, and any molecular mechanics force fields used in the workflow.

## Next steps

After this placeholder is adapted, add a full energy analysis or QM/MM setup
tutorial.
