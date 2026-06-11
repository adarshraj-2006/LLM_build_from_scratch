# Import required modules
import subprocess
import sys
import pathlib
import argparse
import shlex

# Get the directory where this script is located
ROOT = pathlib.Path(__file__).resolve().parent

# Path for output folder
OUT = ROOT / "out"


def run(cmd: str):
    """
    Execute a shell command.
    Exit the program if the command fails.
    """
    print(f"\n>>> {cmd}")

    # Run command from project root directory
    res = subprocess.run(shlex.split(cmd), cwd=ROOT)

    # Stop execution if command returns an error
    if res.returncode != 0:
        sys.exit(res.returncode)


def main():
    """
    Main function that runs demos and tests.
    """

    # Create command-line argument parser
    p = argparse.ArgumentParser()

    # Optional flag:
    # python orchestrator.py --visualize
    p.add_argument(
        "--visualize",
        action="store_true",
        help="Run visualization scripts and save PNGs to ./out"
    )

    # Parse command-line arguments
    args = p.parse_args()

    # Create output directory if it doesn't exist
    OUT.mkdir(exist_ok=True)

    # Run NumPy attention demo
    run("python attn_numpy_demo.py")

    # Run attention math unit tests
    run("python -m pytest -q tests/test_attn_math.py")

    # Run causal mask unit tests
    run("python -m pytest -q tests/test_causal_mask.py")

    # Run visualization script only if --visualize flag is provided
    if args.visualize:
        run("python demo_visualize_multi_head.py")
        print(f"\nVisualization images saved to: {OUT}")

    # Final success message
    print("\nAll Part 1 demos/tests completed. ✅")


# Entry point of the program
if __name__ == "__main__":
    main()