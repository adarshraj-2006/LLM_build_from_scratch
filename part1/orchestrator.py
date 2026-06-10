import subprocess, sys,pathlib,argparse,shlex

ROOT=pathlib.Path(_file_).resolve().parent
OUT =ROOT / "out"

def run(cmd: str):
    print(f"\n>>> {cmd}")
    res=subprocess.run(shlex.split(cmd), cwd=ROOT)
    if res.returncode !=0:
        sys.exit(res.returncode)
def main():
    p=argparse.ArguementParser()
    p.add_argument("--visualize",action = "store_true",help="run visualization scripts and save PNGs to ./out")
    args=p.parse_args()

    OUT.mkdir(exist_ok=True)

    run("python attn_numpy_demo.py")
    run("python -m pytest -q tests/test_attn_math.py")
    run("python -m pytest -q tests/test_casual_mask.py")
        
    if args.visualize:
        run("python demo_visualize_multi_head.py")
        print(f"\nVisualization images saved to: {OUT}")

    print("\nAll Part 1 demos/tests completed. ✅")

if __name__ == "__main__":
    main()
