from argparse import ArgumentParser

from problem import BoggleProblem
from solutions import EliSolution, FernandoSolution
from solutions.daniel import DanielSolution

if __name__ == "__main__":
    # Print usage if no args were given
    """if len(sys.argv) < 3:
        print("Usage:")
        print("boggle.py [--solver=<choice>] [--multi] words.txt board.json")
        print("=================")
        print("Use --solver to specify one of eli, daniel, or fernando")
        print("Defaults to eli")
        print("Use the --multi flag to specify whether multiple boards exist in one json file")
        print("Defaults to false")
        sys.exit(0)"""

    # Parse arguments
    parser = ArgumentParser(
        description='Finds all words in a Boggle board'
    )
    parser.add_argument('words_file', help='Newline-delimited list of words in plaintext file')
    parser.add_argument('board_file', help='2d JSON array representing a single Boggle board, or 3d JSON array representing multiple boards if --multi is specified')
    parser.add_argument('-s', '--solver', choices=['eli', 'daniel', 'fernando'], default='eli', help='choose which solution algorithm to use')
    parser.add_argument('-m', '--multi', help='specify that multiple boards exist in one JSON file (3d array)', action='store_true')
    args = parser.parse_args()
    print(args)

    # Read files
    bp = BoggleProblem(args.words_file, args.board_file, args.multi)

    # Choose solver
    SolutionClass = None
    if args.solver == "eli":
        SolutionClass = EliSolution
    elif args.solver == "daniel":
        SolutionClass = DanielSolution
    elif args.solver == "fernando":
        SolutionClass = FernandoSolution

    # Run the chosen solver
    board_count = 0
    results = []
    print(f"Solving {board_count} boards")
    print("============================")
    print("")
    for i, board in enumerate(bp.boards):
        solution = SolutionClass(bp.words, board)
        found_words = solution.find_words()
        print(f"Board {i}:")
        print(f"Found {len(found_words)} words")
        print(found_words)
        print()
