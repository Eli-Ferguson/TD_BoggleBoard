import sys

from problem import BoggleProblem_Old, BoggleProblem
from Solver import Solution


def runOld():
    # Get File Paths From Args
    BoardFile, wordsFile = sys.argv[1], sys.argv[2]

    # Read Boards and Words From Files
    BP = BoggleProblem_Old(words_file=wordsFile, board_file=BoardFile)

    # Create and set params
    S = Solution(board=BP.board, letterDict=BP.letter_dict)

    # Find Solutions
    print(f'Words Found: {S.findWordsInBoggle( BP.words )}')
    return


def run():
    # Get File Paths From Args
    boards_file, words_file = sys.argv[1], sys.argv[2]
    wordsFound = []
    # Read Boards and Words From Files
    BP = BoggleProblem(boards_file, words_file)
    for i, board in enumerate(BP.boards):
        # Create and set params
        S = Solution(board, words=BP.words)
        # Solve boggleboard
        print(f'Solving Board {i}, {len(board)}x{len(board[0])}')
        print('-----------------------')
        wordsFound.append(S.runBruteForce(board)[1])
        print()
    return wordsFound


if __name__ == '__main__':
    run()
