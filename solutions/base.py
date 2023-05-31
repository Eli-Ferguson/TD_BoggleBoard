from abc import ABC, abstractmethod
from typing import List


class SolutionBase(ABC):
    words: List[str]
    board: List[List[str]]

    def __init__(self, words: List[str], board: List[List[str]]):
        """
        Class representing a solver for the Boggle problem
        
        Parameters
        ----------
        words : A list of words to search the board for
        board : A 2d array of characters representing the Boggle board
        """
        self.words = words
        self.board = board

    @abstractmethod
    def find_words(self) -> List[str]:
        """
        Find the words in the board

        Returns
        -------
        A list of words that were found on the board
        """
        pass
