import random
import time

directionX = [0, 1, 0, -1, 1, 1, -1, -1]
directionY = [1, 0, -1, 0, 1, -1, 1, -1]
allWords = []
N = 0
board = []


class Solution_BruteForce:

    # Perform an exhaustive dfs looking for the word
    def DFS(self, word, i, j, wordIdx):
        if self.outBounds(i, j):
            return False

        if wordIdx == len(word):
            return True

        if word[wordIdx] != board[i][j]:
            return False

        for k in range(0, len(directionX)):
            if self.DFS(word, i+k, j+k, wordIdx+1):
                return True

        return False

    def outBounds(self, i, j):
        return i < 0 or j < 0 or i >= N or j >= N


# TODO - Optimized Solution
class Solution_Optimized:
    def DFS(word, i, j, wordIdx):
        return


def findStartingPositions(letter):
    positions = []
    for i in range(0, N):
        for j in range(0, N):
            if (board[i][j] == letter):
                positions.append((i, j))
    return positions


def setUp():
    # Read words
    file = open('./words.txt', 'r')
    for line in file.readlines():
        word = line.strip().lower()
        allWords.append(word)

    global N
    N = random.randint(100, 250)
    global board
    board = [[chr(random.randrange(97, 122)) for i in range(0, N)]
             for j in range(0, N)]


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
