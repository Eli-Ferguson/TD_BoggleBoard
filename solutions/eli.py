from collections import defaultdict
from typing import Dict, List

from solutions.base import SolutionBase


class EliSolution(SolutionBase):

    letters_dict: Dict[str, List[List[int]]]
    rows: int
    cols: int
    traveled: List[List[int]]

    def __init__(self, words: List[str], board: List[List[str]]):
        # Call super method
        super().__init__(words, board)

        # Initialize solutions-specific variables
        self.letters_dict = defaultdict(list)
        for y, row in enumerate(self.board):
            for x, letter in enumerate(row):
                self.letters_dict[letter].append([y, x])

        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.traveled = []

    def dfs(self, r: int, c: int, word: str) -> int:
        """
        Recursively performs a depth-first search on the Boggle board for a given word

        Parameters
        ----------
        r : Row to DFS on
        c : Column to DFS on
        word : Remaining portion of word to search for

        Returns
        -------
        0 or 1 depending on whether the DFS was successful
        """

        # Make sure we don't double back
        if [r, c] in self.traveled:
            return 0
        else:
            self.traveled.append([r, c])

        if self.board[r][c] == word[0]:
            # Base case: if we found the last character of the word, it's a match
            if len(word) == 1:
                return 1

            # Up
            if r > 0 and self.dfs(r-1, c, word[1:]): return 1
            # Down
            if r < self.rows and self.dfs(r+1, c, word[1:]): return 1
            # Left
            if c > 0 and self.dfs(r, c-1, word[1:]): return 1
            # Right
            if c < self.cols and self.dfs(r, c+1, word[1:]): return 1
            # Up-left
            if (r > 0 and c > 0) and self.dfs(r-1, c-1, word[1:]): return 1
            # Up-right
            if(r > 0 and c < self.cols) and self.dfs(r-1, c+1, word[1:]): return 1
            # Down-left
            if(r < self.rows and c > 0) and self.dfs(r+1, c-1, word[1:]): return 1
            # Down-right
            if(r < self.rows and c < self.cols) and self.dfs(r+1, c+1, word[1:]): return 1

            # Backtrack self-traveled if no adjacent path was found
            self.traveled.pop(-1)
            return 0

        else:  # This wasn't the next letter in the word
            self.traveled.pop(-1)
            return 0

    def find_words(self) -> List[str]:
        # Initiate word count
        words_found = []

        for word in self.words:

            # Make sure all the letters of the word actually exist on the board
            passed = [letter for letter in word if letter not in self.letters_dict]

            # If so (i.e. passed is an empty list because no missing letters were found)
            if not passed:
                for pos in self.letters_dict[word[0]]:
                    self.traveled = []
                    if self.dfs(pos[0], pos[1], word):
                        words_found.append(word)
                        break

        return words_found
