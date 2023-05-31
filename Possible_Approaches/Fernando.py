import random
import time
import json
from typing import List, Tuple, Dict

BoggleBoard = List[List[str]]

directionRow: List[int] = [0, 1, 0, -1, 1, 1, -1, -1]
directionCol: List[int] = [1, 0, -1, 0, 1, -1, 1, -1]
allWords: List[str] = []
boards: List[BoggleBoard] = []
dict: Dict[Tuple[int, int], Dict[str, List[Tuple[int, int]]]] = {}
MAX_BOARD_WIDTH = 250


class Solution_BruteForce:
    def DFS(self, board: BoggleBoard, word: str, row: int, col: int, wordIdx: int, visited: List[List[bool]]):
        if wordIdx == len(word):
            return True

        if outBounds(board, row, col) or (word[wordIdx] != board[row][col]) or visited[row][col]:
            return False

        visited[row][col] = True

        for k in range(0, len(directionRow)):
            newRow = row+directionRow[k]
            newCol = col+directionCol[k]
            if self.DFS(board, word, newRow, newCol, wordIdx+1, visited):
                return True

        visited[row][col] = False

        return False


class Solution_Optimized:
    def DFS(self, board: BoggleBoard, word: int, row: int, col: int, wordIdx: int, visited: List[List[bool]]):

        if wordIdx == len(word)-1:
            return True

        if visited[row][col] or (word[wordIdx+1] not in dict[(row, col)]):
            return False

        visited[row][col] = True

        for position in dict[(row, col)][word[wordIdx+1]]:
            if self.DFS(board, word, position[0], position[1], wordIdx+1, visited):
                return True

        visited[row][col] = False
        return False


def findStartingPositions(board: BoggleBoard, letter: str):
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


def outBounds(board: BoggleBoard, i: int, j: int):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])


def run_BruteForce(board: BoggleBoard):
    """
    Run brute force implementation of Boggle

    :param board: The BoggleBoard being solved
    """

    Sol_BF = Solution_BruteForce()
    wordsFound = 0
    startTime = time.time()

    for word in allWords:
        startingPositions = findStartingPositions(board, word[0])
        if len(startingPositions) > 0:
            for pos in startingPositions:
                visited = [[False]*len(board)]*len(board)
                res = Sol_BF.DFS(board, word, pos[0], pos[1], 0, visited)
                if res:
                    wordsFound += 1
                    break

    elaspedTime = time.time() - startTime
    print(
        f"Brute Force Approach: {wordsFound}/{len(allWords)} words found. Time elapsed: {elaspedTime: 0.3f}s")
    return elaspedTime, wordsFound


def run_Optimized(board: BoggleBoard):
    """
    Run optimized implementation of Boggle

    :param board: The BoggleBoard being solved
    """
    Sol_Op = Solution_Optimized()
    wordsFound = 0

    # Set up dictionary for fast lookups for optimized approach
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            dict[(row, col)] = {}
            for k in range(0, len(directionRow)):
                newRow = row+directionRow[k]
                newCol = col+directionCol[k]
                if not outBounds(board, newRow, newCol):
                    if board[newRow][newCol] not in dict[(row, col)]:
                        dict[(row, col)][board[newRow][newCol]] = []
                    dict[(row, col)][board[newRow][newCol]
                                     ].append((newRow, newCol))

    startTime = time.time()

    for word in allWords:
        startingPositions = findStartingPositions(board, word[0])
        if len(startingPositions) > 0:
            for pos in startingPositions:
                visited = [[False]*len(board)]*len(board)
                res = Sol_Op.DFS(board, word, pos[0], pos[1], 0, visited)
                if res:
                    wordsFound += 1
                    break

    elapsedTime = time.time() - startTime
    print(
        f"Optimized Approach: {wordsFound}/{len(allWords)} words found. Time elapsed: {elapsedTime:0.3f}s")
    return elapsedTime, wordsFound


def generateBoards(numBoards: int):
    """
    Generates a set of numBoards number of boggleboards with random letters

    :param numBoards: Number of boggleboards to generate
    """

    print("Generating boggle boards...")
    for i in range(0, numBoards):
        N = random.randrange(5, MAX_BOARD_WIDTH)  # boards of varying lengths
        board = [[chr(random.randrange(97, 123)) for _ in range(0, N)]
                 for _ in range(0, N)]
        boards.append(board)
        print(f"Generated board {i}, {N}x{N}")
    print()
    return boards


def readInBoards(path: str):
    """
    Reads in a set of boggleboards

    :param path: Path to json file containing the board input
    """
    with open(path, 'r') as f:
        input = json.load(f)
        for board in input['boards']:
            boards.append(board)
    return


def readInWords(path: str):
    """
    Reads in a set of words to use as the word bank for Boggle

    :param path: Path to json file containing the words
    """

    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().lower()
            allWords.append(word)
    return


def main():
    readInWords('./words.txt')
    generateBoards(10)
    for i in range(0, len(boards)):
        board = boards[i]
        print(f"Solving Board {i}, {len(board)}x{len(board[0])}...")
        result1 = run_BruteForce(board)
        result2 = run_Optimized(board)
        dict.clear()
        print(
            f'Optimized version is {1/(result2[0]/result1[0]):0.3f}x faster than brute force')
        print()
    return


if __name__ == '__main__':
    main()
