# 🎨 Paint on Wordle

[![PyPI version](https://img.shields.io/pypi/v/paint-on-wordle?style=flat-square)](https://pypi.org/project/paint-on-wordle/)
[![PyPI downloads](https://img.shields.io/pypi/dm/paint-on-wordle?style=flat-square)](https://pypi.org/project/paint-on-wordle/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/pypi/l/paint-on-wordle?style=flat-square)](https://opensource.org/licenses/MIT)

**Make Wordle look exactly how you want!**

Paint on Wordle is a powerful solver tool that allows you to reverse-engineer the game. Instead of guessing words to find a solution, you provide the **colors** (pattern) and the **solution word**, and the tool tells you exactly which words you need to type to create that pattern on the grid.

Perfect for creating specific shapes/pixel art on your Wordle grid or solving tricky scenarios.

## Features

*   **🧙 Interactive Wizard:** A step-by-step graphical terminal interface to build your grid visually.
*   **⚡ Instant Solution Mode:** Get immediate results by providing arguments directly in the command line.
*   **🧠 Flexible Matching:** Smart algorithm that prioritizes exact matches but can swap Yellow/Green colors to find the closest possible word for your pattern.
*   **🔍 Exhaustive Search:** Ability to list *all* valid candidates for a pattern, not just the best one.

## Installation

Install the package directly from PyPI:

```bash
pip install paint-on-wordle
```

## Usage

Once installed, you can run the tool using the command `paint-wordle`.

### 1. Interactive Wizard (Default)

Run without any arguments to start the interactive mode. The tool will guide you through setting the target word and painting the grid row by row.

```bash
paint-wordle
```

**Controls:**
*   **Arrows / WASD**: Move cursor between tiles.
*   **Space**: Toggle tile color (⬛ Gray -> 🟨 Yellow -> 🟩 Green).
*   **Enter**: Confirm pattern and find matching words.
*   **Esc**: Exit the program.

### 2. Instant Solution Mode

Use command-line arguments to skip the wizard and get immediate answers. This is useful for scripting or quick lookups.

**Required Arguments:**
*   `--word` / `-w`: The hidden target word (the solution) relative to which patterns are calculated.
*   `--pattern` / `-p`: One or more color patterns to match (e.g., `20010`).

**Pattern Legend:**
*   `0` = Gray (Miss)
*   `1` = Yellow (Wrong Spot)
*   `2` = Green (Exact Match)

#### Advanced Options:

*   **`--flexible` / `-f` (Smart Matching)**
    By default, the solver is strict. If you use this flag, it treats Green and Yellow as interchangeable hits while strictly enforcing Gray spots.
    
    *Logic:* It searches for an **exact match first**. If none exists, it finds the closest match by performing the minimum number of color swaps necessary.

*   **`--find-all` / `-a`**
    Lists **all** valid candidates found for each pattern instead of showing only the single best word.

### Examples

**Basic Exact Match:**
Find a word that generates "Green, Gray, Gray, Gray, Gray" when the solution is "apple":
```bash
paint-wordle --word apple --pattern 20000
```

**Multiple Patterns:**
Check three different rows at once:
```bash
paint-wordle -w apple -p 20000 00100 22222
```

**Using Flexible Mode:**
You want a specific pattern, but you don't care if some Yellows become Greens (or vice versa), as long as the Grays stay Gray:
```bash
paint-wordle -w apple -p 21001 --flexible
```

**List All Candidates:**
Show every single word that fits the pattern, not just the first one found:
```bash
paint-wordle -w apple -p 00000 --find-all
```

## Development

If you want to contribute or run the code from source:

1.  Clone the repository:
    ```bash
    git clone https://github.com/KMChris/paint-on-wordle.git
    cd paint-on-wordle
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run via module:
    ```bash
    python -m src.main
    ```

## Project Structure

*   `src/main.py`: Entry point. Handles argument parsing and mode selection.
*   `src/cli.py`: Handles the interactive wizard interface and user input.
*   `src/solution.py`: Core logic, pattern calculation, and word filtering algorithms.
*   `src/data/words.txt`: The dictionary of valid 5-letter words.
