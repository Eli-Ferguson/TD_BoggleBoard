from collections import defaultdict
from typing import List, Dict, Tuple
import json
import time
import random


class Solution_Old:

    def __init__(self, board, letterDict):

        self.board = board
        self.letterDict = letterDict

        self.rows = len(self.board)-1
        self.cols = len(self.board[0])-1

    def DFS(self, r, c, word):

        if [r, c] in self.traveled:
            return 0
        else:
            self.traveled.append([r, c])

        if self.board[r][c] == word[0]:
            if len(word) == 1:
                return 1

            # up
            if r > 0 and self.DFS(r-1, c, word[1:]):
                return 1
            # down
            if r < self.rows and self.DFS(r+1, c, word[1:]):
                return 1
            # left
            if c > 0 and self.DFS(r, c-1, word[1:]):
                return 1
            # right
            if c < self.cols and self.DFS(r, c+1, word[1:]):
                return 1

            # upLeft
            if (r > 0 and c > 0) and self.DFS(r-1, c-1, word[1:]):
                return 1
            # upRight
            if (r > 0 and c < self.cols) and self.DFS(r-1, c+1, word[1:]):
                return 1
            # downLeft
            if (r < self.rows and c > 0) and self.DFS(r+1, c-1, word[1:]):
                return 1
            # downRight
            if (r < self.rows and c < self.cols) and self.DFS(r+1, c+1, word[1:]):
                return 1

            self.traveled.pop(-1)
            return 0

        else:
            self.traveled.pop(-1)
            return 0

    def findWordsInBoggle(self, words):

        wordsFoundCount = 0
        for word in words:

            passed = [letter for letter in word if letter not in self.lettersDict]

            if not passed:

                b = False

                for pos in self.lettersDict[word[0]]:

                    self.traveled = []

                    if self.DFS(pos[0], pos[1], word):
                        # print( f'Found: {word} @ {pos} with {self.traveled}' )
                        wordsFoundCount += 1
                        b = True
                        break

                if not b:
                    print(f'Not Found: {word}')

        return wordsFoundCount


class Solution:
    BoggleBoard = List[List[str]]
    directionRow: List[int] = [0, 1, 0, -1, 1, 1, -1, -1]
    directionCol: List[int] = [1, 0, -1, 0, 1, -1, 1, -1]
    allWords: List[str]
    board: BoggleBoard
    dict: Dict[Tuple[int, int], Dict[str, List[Tuple[int, int]]]] = {}
    MAX_BOARD_WIDTH = 200

    def __init__(self, board: str, words: str) -> None:
        if board:
            self.board = board
        else:
            self.generateBoard()

        self.allWords = words
        return

    def generateBoard(self):
        """
        Generates a Boggleboard with random letters

        """

        print("Generating boggle board...")
        # boards of varying lengths
        N = random.randrange(5, self.MAX_BOARD_WIDTH)
        board = [[chr(random.randrange(97, 123)) for _ in range(0, N)]
                 for _ in range(0, N)]
        self.board = board
        print(f"Generated board, {N}x{N}\n")
        return

    def dfs_bruteForce(self, board: BoggleBoard, word: str, row: int, col: int, wordIdx: int, visited: List[List[bool]]):
        if wordIdx == len(word):
            return True

        if self.outBounds(board, row, col) or (word[wordIdx] != board[row][col]) or visited[row][col]:
            return False

        visited[row][col] = True

        for k in range(0, len(self.directionRow)):
            newRow = row+self.directionRow[k]
            newCol = col+self.directionCol[k]
            if self.dfs_bruteForce(board, word, newRow, newCol, wordIdx+1, visited):
                return True

        visited[row][col] = False

        return False

    def dfs_optimized(self, board: BoggleBoard, word: int, row: int, col: int, wordIdx: int, visited: List[List[bool]]):

        if wordIdx == len(word)-1:
            return True

        if visited[row][col] or (word[wordIdx+1] not in self.dict[(row, col)]):
            return False

        visited[row][col] = True

        for position in self.dict[(row, col)][word[wordIdx+1]]:
            if self.dfs_optimized(board, word, position[0], position[1], wordIdx+1, visited):
                return True

        visited[row][col] = False
        return False

    def outBounds(self, board: BoggleBoard, i: int, j: int):
        return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])

    def findStartingPositions(self, board: BoggleBoard, letter: str):
        """
        Used to find all positions where a letter exists in order to start the DFS search

        :param board: The BoggleBoard being solved
        :param letter: The first letter of the word being searched for
        """

        positions = []
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if (board[i][j] == letter):
                    positions.append((i, j))
        return positions

    def runBruteForce(self, board: BoggleBoard):
        wordsFound = 0
        startTime = time.time()
        for word in self.allWords:
            startingPositions = self.findStartingPositions(board, word[0])
            if len(startingPositions) > 0:
                for pos in startingPositions:
                    visited = [[False]*len(board)]*len(board)
                    res = self.dfs_bruteForce(
                        board, word, pos[0], pos[1], 0, visited)
                    if res:
                        wordsFound += 1
                        break

        elaspedTime = time.time() - startTime
        print(
            f"Brute Force Approach: {wordsFound}/{len(self.allWords)} words found. Time elapsed: {elaspedTime: 0.3f}s")
        return elaspedTime, wordsFound

    def runOptimized(self, board: BoggleBoard):
        wordsFound = 0

        # Set up dictionary for fast lookups for optimized approach
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                self.dict[(row, col)] = {}
                for k in range(0, len(self.directionRow)):
                    newRow = row+self.directionRow[k]
                    newCol = col+self.directionCol[k]
                    if not self.outBounds(board, newRow, newCol):
                        if board[newRow][newCol] not in self.dict[(row, col)]:
                            self.dict[(row, col)][board[newRow][newCol]] = []
                        self.dict[(row, col)][board[newRow][newCol]
                                              ].append((newRow, newCol))

        startTime = time.time()

        for word in self.allWords:
            startingPositions = self.findStartingPositions(board, word[0])
            if len(startingPositions) > 0:
                for pos in startingPositions:
                    visited = [[False]*len(board)]*len(board)
                    res = self.dfs_optimized(
                        board, word, pos[0], pos[1], 0, visited)
                    if res:
                        wordsFound += 1
                        break

        elaspedTime = time.time() - startTime
        print(
            f"Brute Force Approach: {wordsFound}/{len(self.allWords)} words found. Time elapsed: {elaspedTime: 0.3f}s")
        return elaspedTime, wordsFound

    def main(self):
        print(f"Solving Board, {len(self.board)}x{len(self.board[0])}...")
        result1 = self.runBruteForce(self.board)
        result2 = self.runOptimized(self.board)
        self.dict.clear()
        print(
            f'Optimized version is {1/(result2[0]/result1[0]):0.3f}x faster than brute force')
        print()
        return
