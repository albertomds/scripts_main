"""Reusable tutorial script template for CODEX_allScripts.

This file is a starting point for new computational chemistry tutorials. Copy
it into a new tutorial folder, rename it, and replace the placeholder logic with
the real workflow.
"""

from pathlib import Path


TUTORIAL_NAME = "new_tutorial"
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "inputs"
OUTPUT_DIR = BASE_DIR / "outputs"


def describe_tutorial() -> None:
    """Print the tutorial purpose and expected local edits."""
    print(f"Tutorial: {TUTORIAL_NAME}")
    print("This is a template. Edit paths, model choices, and run parameters.")
    print(f"Expected input folder: {INPUT_DIR}")
    print(f"Expected output folder: {OUTPUT_DIR}")


def validate_inputs() -> None:
    """Check that the expected input/output folders exist."""
    for folder in (INPUT_DIR, OUTPUT_DIR):
        if not folder.exists():
            raise FileNotFoundError(f"Missing folder: {folder}")


def main() -> None:
    """Run the tutorial template."""
    describe_tutorial()
    validate_inputs()
    print("Template check complete. Add calculation-specific code here.")


if __name__ == "__main__":
    main()
