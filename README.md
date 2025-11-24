# Paint on Wordle

A simple and effective Wordle solver tool written in Python. The program allows you to "paint" the color pattern (gray, yellow, green) for a given word and finds all matching solutions based on that.

## Features

*   **Interactive CLI Mode:** A graphical terminal interface where you can select tile colors.
*   **Command Line Mode:** Quick solution lookup by providing arguments at runtime.
*   **Filtering Algorithm:** Precise word matching based on Wordle rules (accounts for letter repetitions).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/KMChris/paint-on-wordle.git
    cd paint-on-wordle
    ```

2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Interactive Mode (CLI)

Run the program without arguments:

```bash
python main.py
```

1.  Enter the **solution** word (or a test word against which you are checking other words).
2.  Use the keyboard to control the grid:
    *   **Arrows / WASD:** Move cursor.
    *   **Space:** Toggle tile color (⬛ Gray -> 🟨 Yellow -> 🟩 Green).
    *   **Enter:** Confirm pattern and find matching words.
    *   **Esc:** Exit.

### 2. Command Line Mode

You can use the `--target` (target word) and `--pattern` (color pattern) flags to quickly get results.

**Pattern Legend:**
*   `0` = Gray (letter not in word / wrong spot)
*   `1` = Yellow (correct letter, wrong spot)
*   `2` = Green (correct letter, correct spot)

**Examples:**

Find words that, for the target "apple", result in "green, gray, gray, gray, gray":
```bash
python main.py --target apple --pattern 20000
```

Check multiple patterns at once:
```bash
python main.py -t apple -p 20000 22222
```

## Project Structure

*   `main.py`: Main entry point for the program.
*   `src/cli.py`: Handles user interface and keyboard input.
*   `src/solution.py`: Solving logic and word filtering.
*   `src/data/words.txt`: Word database (dictionary).
