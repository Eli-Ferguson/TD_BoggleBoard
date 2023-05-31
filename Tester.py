import json
import unittest
import Runner


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BOARD_ANSWERS = readInBoardAnswers('./answers.json')
        return

    def test(self):
        wordsFound = Runner.run()
        for i, count in enumerate(wordsFound):
            self.assertEqual(self.BOARD_ANSWERS[i], count)
        return


def readInBoardAnswers(path: str):
    answers = []
    with open(path, 'r') as f:
        input = json.load(f)
        for answer in input['answers']:
            answers.append(answer)
    return answers


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
