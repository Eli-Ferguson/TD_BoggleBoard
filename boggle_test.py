import json
import os
import unittest
from argparse import ArgumentParser
from typing import List, Type, Tuple

from solutions import SolutionBase
from problem import BoggleProblem
from solutions import EliSolution, FernandoSolutionBrute
from solutions.daniel import DanielSolution


class TestSolution:
    name: str
    description: str
    words: List[str]
    boards: List[List[List[str]]]
    answers: List[List[str]]
    SolutionClass: Type[SolutionBase]

    def __init__(self, name, description, words, boards, answers, soln_class: Type[SolutionBase]):
        super().__init__()
        self.name = name
        self.description = description
        self.words = words
        self.boards = boards
        self.answers = answers
        self.SolutionClass = soln_class

    def test(self) -> Tuple[List[str], List[str]]:
        # Iterate over all boards
        for board, answer in zip(self.boards, self.answers):
            # Run the solver
            solution = self.SolutionClass(self.words, board)
            found_words = solution.find_words()
            # Check that all words that were found were supposed to have been found
            bad_words = []
            for fw in found_words:
                if fw not in answer:
                    bad_words.append(fw)
            # Check that all words that were supposed to have been found were indeed found
            missing_words = []
            for word in answer:
                if word not in found_words:
                    missing_words.append(word)

            return bad_words, missing_words


def main(args):
    # Find all subdirectories of the test directory
    subdirs = [f.path for f in os.scandir(args.testdir) if f.is_dir()]

    # Run tests
    print(f"Running {len(subdirs)} tests")
    print("============================")
    for i, testdir in enumerate(subdirs):
        desc_path = os.path.join(testdir, 'description.txt')
        words_path = os.path.join(testdir, 'words.txt')
        board_path = os.path.join(testdir, 'board.json')
        answers_path = os.path.join(testdir, 'answer.json')

        # Create `BoggleProblem` instance using words, boards, and answers files
        bp = BoggleProblem(words_path, board_path, answers_path, multi_board=True)

        # Define the name and description of the test
        name = os.path.basename(testdir)
        with open(desc_path, 'r') as df:
            description = df.read()

        # Determine which solution to use
        soln_class = None
        if args.solver == 'eli':
            soln_class = EliSolution
        elif args.solver == 'daniel':
            soln_class = DanielSolution
        elif args.solver == 'fernando':
            soln_class = FernandoSolutionBrute
        test = TestSolution(name, description, bp.words, bp.boards, bp.answers, soln_class)
        # print("\n")
        print(f"Test {i}: {test.name}")
        print(test.description)
        bad_words, missing_words = test.test()
        if len(bad_words) == 0 and len(missing_words) == 0:
            print("Test passed!")
        else:
            print(f"Found words that weren't in the answer: {bad_words}")
            print(f"Words in the answer that weren't found by the solver: {missing_words}")
        print("---------------------------------")


if __name__ == "__main__":
    # Parse arguments and call main function
    parser = ArgumentParser(
        description='Tests one algorithm at a time'
    )
    parser.add_argument('-s', '--solver', choices=['eli', 'daniel', 'fernando'], help='choose which solution algorithm to test', required=True)
    parser.add_argument('-t', '--testdir', default='./test', help='directory to find the tests in')
    main(parser.parse_args())
