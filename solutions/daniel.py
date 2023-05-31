from collections import defaultdict
from typing import Dict, List, Tuple

from solutions.base import SolutionBase


class DanielSolution(SolutionBase):

    letter_dict: Dict[str, List[Tuple[int, int]]]
    traversed: List[Tuple[int, int]]

    def __init__(self, words: List[str], board: List[List[str]]):
        # Call super method
        super().__init__(words, board)

        # Initialize solution-specific variables
        self.letter_dict = defaultdict(list)
        for y, row in enumerate(self.board):
            for x, letter in enumerate(row):
                self.letter_dict[letter].append((x, y))

    def substring_exists(self, sub: str, pos: Tuple[int, int]) -> bool:
        first_letter = sub[0]
        # Check adjacency of the current letter to the position of the previous letter
        oldx, oldy = pos
        for coord in self.letter_dict[first_letter]:
            # Check whether this space was already used
            if coord in self.traversed:
                continue
            newx, newy = coord
            # Check adjacency
            if (abs(oldx - newx) <= 1) and (abs(oldy - newy) <= 1) and (not (oldx == newx and oldy == newy)):
                # Base case, last letter in word
                if len(sub) == 1:
                    return True
                # Otherwise, recurse
                self.traversed.append(coord)
                if self.substring_exists(sub[1:], coord):
                    return True
        return False

    def word_exists(self, word: str) -> bool:
        # Check whether any letters are missing
        for letter in word:
            if letter not in self.letter_dict:
                return False

        # Iterate over all starting positions, searching for the word
        found = False
        for start_pos in self.letter_dict[word[0]]:
            self.traversed = [start_pos]
            if self.substring_exists(word[1:], start_pos):
                found = True
                break
        return found

    def find_words(self) -> List[str]:
        found_words = []
        for word in self.words:
            if self.word_exists(word):
                found_words.append(word)
        return found_words
