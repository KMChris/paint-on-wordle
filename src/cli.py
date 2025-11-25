from pynput import keyboard
from solution import Solution

GRID_WIDTH = 5
GRID_HEIGHT = 6

TILE_STATES = ["⬛", "🟨", "🟩"]
DOT_STATES = ["⚫", "🟡", "🟢"]

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.cursor_x = 0
        self.cursor_y = 0
        self._drawn_once = False

    def toggle_cell(self):
        current = self.grid[self.cursor_y][self.cursor_x]
        self.grid[self.cursor_y][self.cursor_x] = (current + 1) % len(TILE_STATES)

    def move_cursor(self, dx, dy):
        self.cursor_x = (self.cursor_x + dx) % self.width
        self.cursor_y = (self.cursor_y + dy) % self.height

    def draw(self, show_cursor=True):
        if not self._drawn_once:
            print("Use the arrow keys to move, the space bar to select, and Enter to accept.")
            self._drawn_once = True
        else:
            print(f"\x1B[{self.height}A", end="")

        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                state = self.grid[y][x]
                is_cursor = self.cursor_y == y and self.cursor_x == x

                if is_cursor and show_cursor:
                    cell_char = DOT_STATES[state]
                else:
                    cell_char = TILE_STATES[state]

                row_str += f"{cell_char}"
            print(row_str)

def print_words(words, find_all):
    if find_all:
        print("Matching words:")
        for i, word in enumerate(words, 1):
            if word:
                content = ", ".join(w.upper() for w in word)
                print(f"{i}. {content}")
            else:
                print(f"{i}. No matches found.")
    else:
        if words is None:
            print("No matching words found.")
        elif not words:
            print("No constraints provided.")
        else:
            print("Matching words:")
            for i, word in enumerate(words, 1):
                print(f"{i}.", word.upper() if word else "No match")

def main(find_all=False, flexible=False):
    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    solution = Solution(input("Enter the solution word: "))

    def on_press(key):
        char = getattr(key, "char", None)
        if isinstance(char, str):
            char = char.lower()
        try:
            if key == keyboard.Key.up or char == 'w':
                grid.move_cursor(0, -1)
            elif key == keyboard.Key.down or char == 's':
                grid.move_cursor(0, 1)
            elif key == keyboard.Key.left or char == 'a':
                grid.move_cursor(-1, 0)
            elif key == keyboard.Key.right or char == 'd':
                grid.move_cursor(1, 0)
            elif key == keyboard.Key.space:
                grid.toggle_cell()
            elif key == keyboard.Key.enter:
                grid.draw(show_cursor=False)
                words = solution.find_solution(grid.grid, find_all, flexible)
                print_words(words, find_all)
                return False
            elif key == keyboard.Key.esc:
                return False
        except AttributeError:
            pass  # ignore other keys
        grid.draw()

    with keyboard.Listener(on_press=on_press, suppress=True) as listener:
        grid.draw()
        listener.join()

if __name__ == "__main__":
    main()
