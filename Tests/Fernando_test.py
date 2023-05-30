

import sys
import json
import os
import unittest

sys.path.append(os.path.abspath(
    os.getcwd() + '/../Possible_Approaches/'))

import Fernando as Solution_Fernando

class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Solution_Fernando.readInWords('../Possible_Approaches/words.txt')
        Solution_Fernando.readInBoards('./tests_Fernando.json')
        cls.BOARD_ANSWERS = readInBoardAnswers('./tests_Fernando.json')
        return
    
    def test(self):
        for i in range(0, len(Solution_Fernando.boards)):
            result = Solution_Fernando.run_BruteForce(Solution_Fernando.boards[i])
            self.assertEqual(self.BOARD_ANSWERS[i], result[1])
        return

def readInBoardAnswers(path: str):
    answers = []
    with open(path, 'r') as f:
        input = json.load(f)
        for answer in input['answers']:
            answers.append(answer)
    return answers
    
if __name__ == '__main__':
    unittest.main()