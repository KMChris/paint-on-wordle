from collections import Counter
import importlib.resources
from . import data

def load_words(filename="words.txt"):
    """
    Loads a list of valid Wordle words from a file.

    Args:
        filename (str): Name of the file in the data directory containing the word list.

    Returns:
        list[str]: A list of stripped, lowercased words.
    """
    resource = importlib.resources.files(data) / filename
    with resource.open('r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_feedback(guess, target):
    """
    Calculates the Wordle color pattern for a given guess against a target word.

    The logic strictly follows Wordle rules:
    1. Green (2): Correct letter in the correct position.
    2. Yellow (1): Correct letter in the wrong position (if available in target).
    3. Gray (0): Letter not in target, or all instances already accounted for.

    Args:
        guess (str): The candidate word being tested.
        target (str): The hidden solution word.

    Returns:
        tuple[int]: A tuple of 5 integers representing colors (0, 1, 2).
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
    """
    Main solver class responsible for finding words that generate specific
    color patterns against a known target word.
    """

    def __init__(self, word):
        self.word = word.lower()
        self._word_list = load_words()
        
    def find_word(self, pattern, find_all=False):
        """
        Finds candidate word(s) that EXACTLY match the given color pattern.

        Args:
            pattern (tuple): The target color pattern (e.g., (2, 0, 0, 1, 0)).
            find_all (bool): If True, returns all matches list; otherwise returns the first match string.

        Returns:
            str | list[str] | None: The found word(s) or None if no exact match exists.
        """
        if not find_all:
            for candidate in self._word_list:
                if get_feedback(candidate, self.word) == pattern:
                    return candidate
            return None
        words = [candidate for candidate in self._word_list
                 if get_feedback(candidate, self.word) == pattern]
        return words

    def find_similar(self, pattern, find_all=False):
        """
        Finds word(s) matching the pattern with flexibility (allowing Yellow/Green swaps).
        
        It prioritizes exact matches (difference = 0). If no exact match is found,
        it minimizes the difference between Yellow (1) and Green (2) while strictly
        enforcing Gray (0) positions.

        Args:
            pattern (tuple): The target color pattern.
            find_all (bool): If True, returns all candidates sorted by relevance (best fit first).

        Returns:
            str | list[str] | None: The best matching word(s) or None if no valid structural match exists.
        """
        best_diff = 6  # max difference is 5
        word = None
        words = []
        for candidate in self._word_list:
            feedback = get_feedback(candidate, self.word)
            diff = 0
            for p, f in zip(pattern, feedback):
                if (p == 0) != (f == 0):
                    diff = 6
                    break
                diff += abs(p - f)
            if find_all and diff < 6:
                words.append((candidate, diff))
            if diff < best_diff:
                best_diff = diff
                word = candidate
        if find_all:
            return [x[0] for x in sorted(words, key=lambda x: x[1])]
        return word

    def find_solution(self, grid, find_all=False, flexible=False):
        """
        Solves for all stored patterns in the grid.

        Args:
            find_all (bool): Return all candidates for each row instead of just one.
            flexible (bool): If True, uses 'find_similar' logic; otherwise uses strict 'find_word'.

        Returns:
            list: A list of results corresponding to each pattern in self.patterns.
        """
        func = self.find_similar if flexible else self.find_word
        return [func(tuple(pattern), find_all) for pattern in grid]
