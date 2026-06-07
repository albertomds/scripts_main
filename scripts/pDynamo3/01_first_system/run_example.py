"""Template for a first pDynamo3 system workflow.

This script is intentionally lightweight. It does not run a real pDynamo3
calculation until you add local inputs and adapt the pDynamo3-specific code for
your installation.
"""

from pathlib import Path


TUTORIAL_NAME = "01_first_system"
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "inputs"
OUTPUT_DIR = BASE_DIR / "outputs"
EXPECTED_INPUT = "system_input_placeholder.ext"
SUMMARY_FILE = OUTPUT_DIR / "template_summary.txt"


def main() -> None:
    """Check the tutorial folders and write a small template summary."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Running template: {TUTORIAL_NAME}")
    print("This is not a production pDynamo3 calculation.")
    print("Edit this script for your local pDynamo3 installation and inputs.")
    print(f"Suggested input placeholder: {INPUT_DIR / EXPECTED_INPUT}")

    input_files = sorted(path.name for path in INPUT_DIR.iterdir() if path.is_file())
    SUMMARY_FILE.write_text(
        "\n".join(
            [
                f"Tutorial: {TUTORIAL_NAME}",
                "Status: template check complete",
                f"Input files detected: {', '.join(input_files) if input_files else 'none'}",
                "Next step: add pDynamo3 system-loading code.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Wrote {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
