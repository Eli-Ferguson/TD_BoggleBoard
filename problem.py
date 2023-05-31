import json
from collections import defaultdict
from typing import List, Optional


class BoggleProblem:
    _words: List[str]
    _boards: List[List[List[str]]]
    _answers: Optional[List[List[str]]]
    multi_board: bool

    def __init__(self, words_file: str, board_file: str, answers_file: str = None, multi_board: bool = False) -> None:
        """
        Represents the state of a single Boggle problem, including the list of words to search for and the board layout

        Parameters
        ----------
        words_file: path to a newline-seperated list of words
        board_file: path to a JSON file with a 2d array of letters representing the Boggle board(s)
        multi_board: Toggle whether multiple boards exist in one JSON file
        """

        # Read the words file, specified as a plain text file with 1 word per line
        with open(words_file, 'r') as wf:
            words = [word.lower().rstrip('\n') for word in wf.readlines()]
            self._words = words

        # Read the board file, specified as a JSON file with 1 top-level 2d array of strings
        self._letter_dict = defaultdict(list)
        with open(board_file) as bf:
            # Read the JSON file
            data = json.load(bf)

            # Wrap it in an outer list of this is a single-board file
            if not multi_board:
                data = [data]

            self._boards = data

            if answers_file:
                with open(answers_file) as af:
                    data = json.load(af)
                    self._answers = data
            else:
                self._answers = None

            self.multi_board = multi_board

    @property
    def words(self) -> List[str]:
        """
        A list of words to search the Boggle board for
        """
        return self._words

    @property
    def boards(self) -> List[List[List[str]]]:
        """
        A 3d list of characters representing the Boggle boards
        """
        return self._boards

    @property
    def answers(self) -> Optional[List[List[str]]]:
        """
        Optional, A 2d list of strings representing the words to be found in each board
        """
        return self._answers
