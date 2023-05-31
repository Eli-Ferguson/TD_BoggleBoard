
import Fernando as Solution_Fernando
import sys
import json
import os

sys.path.append(os.path.abspath(
    os.getcwd() + '/../Possible_Approaches/'))


NUM_TESTCASES_FERNANDO = 10  # used as the number of boards created
Solution_Fernando.MAX_BOARD_WIDTH = 100  # Default is 250


def generateTestCases_Fernando():
    data = {}
    data['boards'] = []
    data['answers'] = []

    Solution_Fernando.readInWords('../Possible_Approaches/words.txt')
    Solution_Fernando.generateBoards(NUM_TESTCASES_FERNANDO)

    for i in range(0, NUM_TESTCASES_FERNANDO):
        board = Solution_Fernando.boards[i]
        data['boards'].append(board)
        result1 = Solution_Fernando.run_BruteForce(board)
        data['answers'].append(result1[1])
        Solution_Fernando.dict.clear()

    with open('tests_Fernando.json', 'w') as f:
        json.dump(data, f)
    return


def main():
    generateTestCases_Fernando()
    return


if __name__ == '__main__':
    main()
