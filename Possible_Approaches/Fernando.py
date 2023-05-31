import random
import time
import json
import sys
from typing import List, Tuple, Dict


class Solution:
    BoggleBoard = List[List[str]]

    directionRow: List[int] = [0, 1, 0, -1, 1, 1, -1, -1]
    directionCol: List[int] = [1, 0, -1, 0, 1, -1, 1, -1]
    allWords: List[str] = []
    boards: List[List[List[str]]] = []
    dict: Dict[Tuple[int, int], Dict[str, List[Tuple[int, int]]]] = {}
    MAX_BOARD_WIDTH = 10

    def __init__(self, boardsFile: str, wordsFile: str) -> None:
        if boardsFile:
            self.readInBoards(boardsFile)
        else:
            self.generateBoards(10)

        self.readInWords(wordsFile)
        return

    def readInBoards(self, path: str):
        """
        Reads in a set of boggleboards

        :param path: Path to json file containing the board input
        """
        with open(path, 'r') as f:
            input = json.load(f)
            print(input)
            for board in input['boards']:
                self.boards.append(board)
        return

    def readInWords(self, path: str):
        """
        Reads in a set of words to use as the word bank for Boggle

        :param path: Path to txt file containing the words
        """

        with open(path, 'r') as f:
            for line in f.readlines():
                word = line.strip().lower()
                self.allWords.append(word)
        return

    def generateBoards(self, numBoards: int):
        """
        Generates a set of numBoards number of boggleboards with random letters

        :param numBoards: Number of boggleboards to generate
        """

        print("Generating boggle boards...")
        for i in range(0, numBoards):
            # boards of varying lengths
            N = random.randrange(5, self.MAX_BOARD_WIDTH)
            board = [[chr(random.randrange(97, 123)) for _ in range(0, N)]
                     for _ in range(0, N)]
            self.boards.append(board)
            print(f"Generated board {i}, {N}x{N}")
        print()
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
        for i in range(0, len(self.boards)):
            board = self.boards[i]
            print(f"Solving Board {i}, {len(board)}x{len(board[0])}...")
            result1 = self.runBruteForce(board)
            result2 = self.runOptimized(board)
            self.dict.clear()
            print(
                f'Optimized version is {1/(result2[0]/result1[0]):0.3f}x faster than brute force')
            print()
        return


if __name__ == '__main__':
    boardsFile, wordsFile = sys.argv[1], sys.argv[2]
    S = Solution(wordsFile, boardsFile)
    S.main()
