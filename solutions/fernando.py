from typing import List, Dict, Tuple

from solutions import SolutionBase


class FernandoSolutionBrute(SolutionBase):
    direction_row: List[int] = [0, 1, 0, -1, 1, 1, -1, -1]
    direction_col: List[int] = [1, 0, -1, 0, 1, -1, 1, -1]
    dict: Dict[Tuple[int, int], Dict[str, List[Tuple[int, int]]]]

    def __init__(self, words: List[str], board: List[List[str]]):
        super().__init__(words, board)

    def find_starting_positions(self, letter: str):
        """
        Used to find all positions where a letter exists in order to start the DFS search

        Parameters
        ----------
        letter : The letter to find all positions for

        Returns
        -------
        A list of coordinates in the board where the letter was found
        """
        positions = []
        for i in range(len(self.board)):
            for j in range(0, len(self.board[0])):
                if self.board[i][j] == letter:
                    positions.append((i, j))
        return positions

    def oob(self, i: int, j: int) -> bool:
        return i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0])

    def dfs_brute(self, word: str, row: int, col: int, word_idx: int, visited: List[List[bool]]):
        # Base case, this is the last letter
        if word_idx == len(word):
            return True

        # Check for out-of-bounds
        if self.oob(row, col) or (word[word_idx] != self.board[row][col]) or visited[row][col]:
            return False

        # Mark current coordinate as visited
        visited[row][col] = True

        # Recurse in all directions
        for k in range(0, len(self.direction_row)):
            new_row = row + self.direction_row[k]
            new_col = col + self.direction_col[k]
            if self.dfs_brute(word, new_row, new_col, word_idx + 1, visited):
                return True

        # All recursive paths failed, unmark as visited
        visited[row][col] = False
        return False

    def find_words(self) -> List[str]:
        found_words = []
        for word in self.words:
            starting_positions = self.find_starting_positions(word[0])
            if len(starting_positions) > 0:
                for pos in starting_positions:
                    visited = [[False] * len(self.board[0])] * len(self.board)
                    res = self.dfs_brute(
                        word, pos[0], pos[1], 0, visited
                    )
                    if res:
                        found_words.append(word)
                        break
        return found_words
