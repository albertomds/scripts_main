"""Placeholder for a pDynamo3 QC single-point energy workflow.

This template only records intended settings. Add real pDynamo3 imports,
system loading, QC model setup, and energy evaluation after selecting local
inputs and confirming your installation.
"""

from pathlib import Path


TUTORIAL_NAME = "02_qc_energy_placeholder"
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "inputs"
OUTPUT_DIR = BASE_DIR / "outputs"
SUMMARY_FILE = OUTPUT_DIR / "qc_energy_template_summary.txt"

QC_MODEL = "edit_me"
TOTAL_CHARGE = 0
MULTIPLICITY = 1
QC_SELECTION = "edit_me_atom_selection"


def main() -> None:
    """Write a placeholder summary for future QC energy calculations."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Running template: {TUTORIAL_NAME}")
    print("This placeholder does not calculate an energy yet.")
    print("Edit the QC settings and add pDynamo3-specific calls before use.")

    SUMMARY_FILE.write_text(
        "\n".join(
            [
                f"Tutorial: {TUTORIAL_NAME}",
                f"QC model: {QC_MODEL}",
                f"Total charge: {TOTAL_CHARGE}",
                f"Multiplicity: {MULTIPLICITY}",
                f"QC selection: {QC_SELECTION}",
                "Status: placeholder only",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Wrote {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
