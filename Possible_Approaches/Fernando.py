import random
import time
import json

directionRow = [0, 1, 0, -1, 1, 1, -1, -1]
directionCol = [1, 0, -1, 0, 1, -1, 1, -1]
allWords = []
boards = []
dict = {}
MAX_BOARD_WIDTH = 250


class Solution_BruteForce:

    # Perform an exhaustive dfs looking for the word
    def DFS(self, board, word, row, col, wordIdx):
        if outBounds(board, row, col):
            return False

        if wordIdx == len(word):
            return True

        if word[wordIdx] != board[row][col]:
            return False

        for k in range(0, len(directionRow)):
            newRow = row+directionRow[k]
            newCol = col+directionCol[k]
            if self.DFS(board, word, newRow, newCol, wordIdx+1):
                return True

        return False


class Solution_Optimized:
    def DFS(self, board, word, row, col, wordIdx):
        if wordIdx == len(word)-1:
            return True

        if word[wordIdx+1] not in dict[(row, col)]:
            return False

        for position in dict[(row, col)][word[wordIdx+1]]:
            if self.DFS(board, word, position[0], position[1], wordIdx+1):
                return True

        return False


def findStartingPositions(board, letter):
    positions = []
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (board[i][j] == letter):
                positions.append((i, j))
    return positions


def outBounds(board, i, j):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])


def run_BruteForce(board):
    Sol_BF = Solution_BruteForce()
    wordsFound = 0
    startTime = time.time()

    for word in allWords:
        startingPositions = findStartingPositions(board, word[0])
        if len(startingPositions) > 0:
            for pos in startingPositions:
                res = Sol_BF.DFS(board, word, pos[0], pos[1], 0)
                if res:
                    wordsFound += 1
                    break

    elaspedTime = time.time() - startTime
    print(
        f"Brute Force Approach: {wordsFound}/{len(allWords)} words found. Time elapsed: {elaspedTime: 0.3f}s")
    return elaspedTime, wordsFound


def run_Optimized(board):
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
                res = Sol_Op.DFS(board, word, pos[0], pos[1], 0)
                if res:
                    wordsFound += 1
                    break

    elapsedTime = time.time() - startTime
    print(
        f"Optimized Approach: {wordsFound}/{len(allWords)} words found. Time elapsed: {elapsedTime:0.3f}s")
    return elapsedTime, wordsFound


def generateBoards(numBoards):
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
    with open(path, 'r') as f:
        input = json.load(f)
        for board in input['boards']:
            boards.append(board)
    return

def readInWords(path: str):
    # Read words  
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
