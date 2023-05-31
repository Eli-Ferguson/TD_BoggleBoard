
import sys
import json
import os

sys.path.append(os.path.abspath(
    os.getcwd() + '/../Possible_Approaches/'))

from Fernando import Solution


def generateTestCases_Fernando():
    dataBoards = {}
    dataAnswers = {}
    dataBoards['boards'] = []
    dataAnswers['answers'] = []

    S = Solution(None, '../Possible_Approaches/words.txt')

    for i in range(0, len(S.boards)):
        board = S.boards[i]
        dataBoards['boards'].append(board)
        result1 = S.runBruteForce(board)
        dataAnswers['answers'].append(result1[1])

    with open('../boards.json', 'w') as f:
        json.dump(dataBoards, f)
    with open('../answers.json', 'w') as f:
        json.dump(dataAnswers, f)
    return


def main():
    generateTestCases_Fernando()
    return


if __name__ == '__main__':
    main()
