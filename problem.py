import json
from collections import defaultdict
from typing import Dict, List, Tuple


class BoggleProblem:
    _words: List[str]
    _board: List[List[str]]
    _letter_dict: Dict[str, List[Tuple[int, int]]]

    def __init__(self, words_file: str, board_file: str) -> None:
        """
        Represents the state of a single Boggle problem, including the list of words to search for and the board layout

        Parameters
        ----------
        words_file: path to a newline-seperated list of words
        board_file: path to a JSON file with a 2d array of letters representing a Boggle board
        """

        # Read the words file, specified as a plain text file with 1 word per line
        with open(words_file, 'r') as wf:
            words = [word.lower().rstrip('\n') for word in wf.readlines()]
            self._words = words

        # Read the board file, specified as a JSON file with 1 top-level 2d array of strings
        self._letter_dict = defaultdict(list)
        with open(board_file) as bf:
            data = json.load(bf)
            for y, row in enumerate(data):
                for x, letter in enumerate(row):
                    self._letter_dict[letter].append((x, y))
            self._board = data

    @property
    def words(self) -> List[str]:
        """
        A list of words to search the Boggle board for
        """
        return self._words

    @property
    def board(self) -> List[List[str]]:
        """
        A 2d list of characters representing the Boggle board
        """
        return self._board

    @property
    def letter_dict(self) -> Dict[str, List[Tuple[int, int]]]:
        """
        A dictionary mapping each letter to a list of board coordinates that letter was found
        """
        return self._letter_dict
