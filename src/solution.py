from collections import Counter

def load_words(filename="words.txt"):
        with open('src/data/' + filename, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

def get_feedback(guess, target):
    """
    Generates feedback for a given guessed word
    relative to the target word.

    Returns a tuple of 5 elements:
    2 - Green
    1 - Yellow
    0 - Gray
    """
    result = [0] * 5
    target_counts = Counter(target)
    
    for i, (g_char, t_char) in enumerate(zip(guess, target)):
        if g_char == t_char:
            result[i] = 2
            target_counts[g_char] -= 1
    for i, g_char in enumerate(guess):
        if result[i] == 0:
            if target_counts[g_char] > 0:
                result[i] = 1
                target_counts[g_char] -= 1
    return tuple(result)

class Solution():
    def __init__(self, word, grid=None):
        self.word = word.lower()
        self.patterns = [] if grid is None else list(grid)
        self._word_list = load_words()
        self.solution = None
    
    def set_grid(self, grid):
        self.patterns = list(grid)
    
    def find_word(self, pattern, find_all=False):
        if not find_all:
            for candidate in self._word_list:
                if get_feedback(candidate, self.word) == pattern:
                    return candidate
            return None
        words = [candidate for candidate in self._word_list
                 if get_feedback(candidate, self.word) == pattern]
        return words

    def find_solution(self, find_all=False):
        return [self.find_word(tuple(pattern), find_all)
                for pattern in self.patterns]
