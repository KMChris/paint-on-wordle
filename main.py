import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

try:
    from src.cli import main as cli_main
    from src.solution import Solution
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def run_solution(target, patterns):
    solver = Solution(target)
    grid = []
    for p in patterns:
        try:
            row = [int(c) for c in p]
            if len(row) != 5:
                raise ValueError("Pattern length must be 5")
            grid.append(row)
        except ValueError:
            print(f"Invalid pattern format: {p}. Use digits 0, 1, 2.")
            sys.exit(1)
            
    solver.set_grid(grid)
    results = solver.find_solution(find_all=True)
    
    print(f"Target Word: {target}")
    for pat, words in zip(patterns, results):
        print(f"Pattern {pat}:")
        if words:
            print(f"  Found {len(words)} matches: {', '.join(words)}")
        else:
            print("  No matches found.")

def main():
    parser = argparse.ArgumentParser(description="Paint on Wordle Solver. Run without arguments to start interactive CLI.")
    parser.add_argument("--target", "-t", type=str, help="The target solution word")
    parser.add_argument("--pattern", "-p", type=str, nargs="+", help="One or more patterns (e.g. 20010)")
    
    args = parser.parse_args()
    
    if args.target and args.pattern:
        run_solution(args.target, args.pattern)
    elif args.target or args.pattern:
        print("Error: Both --target and --pattern are required for solution mode.")
        sys.exit(1)
    else:
        cli_main()

if __name__ == "__main__":
    main()
