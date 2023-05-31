import json
import random
from argparse import ArgumentParser


def main():
    # Parse arguments
    parser = ArgumentParser(
        description='Generate some boggle boards to play'
    )
    parser.add_argument(
        'num_boards', help='number of boards to generate')
    parser.add_argument(
        'max_board_size', help='max size that a board can be, i.e. an NxN board')

    args = parser.parse_args()
    boards = []
    num_boards, max_board_size = int(args.num_boards), int(args.max_board_size)

    # Generate boards
    for i in range(0, num_boards):
        # Assume 5 is smallest board size
        N = random.randrange(5, max_board_size)
        # Add random lowercase letters
        board = [[chr(random.randrange(97, 123))
                  for _ in range(0, N)] for _ in range(0, N)]
        boards.append(board)
        print(f"Generated board {i}")

    with open('./board.json', 'w') as file:
        json.dump(boards, file)

    return


if __name__ == '__main__':
    main()
