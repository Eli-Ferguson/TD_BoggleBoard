import random
import time

directionRow = [0, 1, 0, -1, 1, 1, -1, -1]
directionCol = [1, 0, -1, 0, 1, -1, 1, -1]
allWords = []
N = 0
board = []
dict = {}


class Solution_BruteForce:

    # Perform an exhaustive dfs looking for the word
    def DFS(self, word, row, col, wordIdx):
        if outBounds(row, col):
            return False

        if wordIdx == len(word):
            return True

        if word[wordIdx] != board[row][col]:
            return False

        for k in range(0, len(directionRow)):
            newRow = row+directionRow[k]
            newCol = col+directionCol[k]
            if self.DFS(word, newRow, newCol, wordIdx+1):
                return True

        return False


# TODO - Optimized Solution
class Solution_Optimized:
    def DFS(self, word, i, j, wordIdx):
        return False


def findStartingPositions(letter):
    positions = []
    for i in range(0, N):
        for j in range(0, N):
            if (board[i][j] == letter):
                positions.append((i, j))
    return positions


def outBounds(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


def setUp():
    # Read words
    file = open('./words.txt', 'r')
    for line in file.readlines():
        word = line.strip().lower()
        allWords.append(word)

    global N, board, dict
    N = random.randint(100, 250)
    board = [[chr(random.randrange(97, 123)) for i in range(0, N)]
             for j in range(0, N)]

    # Set up dictionary for fast lookups for optimized approach
    for row in range(0, N):
        for col in range(0, N):
            dict[(row, col)] = {}
            for k in range(0, len(directionRow)):
                newRow = row+directionRow[k]
                newCol = col+directionCol[k]
                if not outBounds(newRow, newCol):
                    if board[newRow][newCol] not in dict[(row, col)]:
                        dict[(row, col)][board[newRow][newCol]] = []
                    dict[(row, col)][board[newRow][newCol]
                                     ].append((newRow, newCol))


def run_SolutionBruteForce():
    setUp()
    Sol_BF = Solution_BruteForce()
    wordsFound = 0
    startTime = time.time()

    for word in allWords:
        # For brute force we search the entire grid to know where to start, there can be multiple
        # starting positions
        startingPositions = findStartingPositions(word[0])
        if len(startingPositions) > 0:
            for pos in startingPositions:
                res = Sol_BF.DFS(word, pos[0], pos[1], 0)
                if res:
                    wordsFound += 1
                    break
    print(
        f"Brute Force Approach: {wordsFound}/{len(allWords)} words found. Board size: {N}x{N}.")
    print(f'Time elapsed: {time.time() - startTime}s')


run_SolutionBruteForce()
