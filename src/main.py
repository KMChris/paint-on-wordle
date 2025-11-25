from .cli import main as cli_main
from .solution import Solution
import argparse
import sys

def run_solution(word, patterns, find_all=False, flexible=False):
    solver = Solution(word)
    grid = []
    for pattern in patterns:
        try:
            row = [int(c) for c in pattern]
            if len(row) != 5:
                raise ValueError("Pattern length must be 5")
            grid.append(row)
        except ValueError:
            print(f"Invalid pattern format: {pattern}. Use digits 0, 1, 2.")
            sys.exit(1)
    
    results = solver.find_solution(grid, find_all, flexible)
    
    print(f"Target Word: {word}")
    for pattern, words in zip(patterns, results):
        print(f"Pattern {pattern}:")
        if words:
            if find_all:
                print(f"  Found {len(words)} matches: {', '.join(words)}")
            else:
                print(f"  Best match: {words}")
        else:
            print("  No matches found.")

def main():
    parser = argparse.ArgumentParser(
        description="Paint on Wordle: Make Wordle look exactly how you want! "
        "Tell me the colors, and I'll tell you the words.\n\n"
        "MODES:\n"
        "1. Interactive Wizard (Default): Run without --word/--pattern arguments. "
        "I will guide you step-by-step to build your grid.\n"
        "2. Instant Solution Mode: Provide --word and --pattern to skip the wizard "
        "and get immediate results.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-w", "--word", type=str,
                        help="The hidden target word (the solution). "
                             "Used to calculate the correct color pattern.\n"
                             "Providing this argument (along with --pattern) triggers "
                             "Instant Solution Mode.")
    parser.add_argument("-p", "--pattern", type=str, nargs="+",
                        help="One or more color patterns to match (e.g. 20010), "
                             "where 0=Gray/Black, 1=Yellow, 2=Green.\n"
                             "Provide multiple patterns separated by space. "
                             "Required for Instant Solution Mode.")
    parser.add_argument("-a", "--find-all", action="store_true",
                        help="Global setting (applies to Wizard & Instant Mode).\n"
                             "List all valid candidates found for each pattern, "
                             "instead of showing only the single best word.")
    parser.add_argument("-f", "--flexible", action="store_true",
                        help="Global setting (applies to Wizard & Instant Mode).\n"
                             "Allow swapping Yellow and Green colors if needed. "
                             "The solver tries to find an exact match first.\n"
                             "If that fails, it looks for the closest match by changing "
                             "as few colors as possible, while keeping Gray spots strictly unchanged.")

    args = parser.parse_args()
    
    if args.word and args.pattern:
        run_solution(args.word, args.pattern, args.find_all, args.flexible)
    elif args.word or args.pattern:
        print("Error: Both --word and --pattern are required for solution mode.")
        sys.exit(1)
    else:
        cli_main(args.find_all, args.flexible)

if __name__ == "__main__":
    main()
