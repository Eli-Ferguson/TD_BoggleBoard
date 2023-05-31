import sys

from problem import BoggleProblem
from Solver import Solution

if __name__ == '__main__' :
    # Get File Paths From Args
    BoardsFile, wordsFile = sys.argv[ 1 ], sys.argv[ 2 ]
    
    # Read Boards and Words From Files
    BP = BoggleProblem( words_file=wordsFile, board_file=BoardsFile )
    
    # Create and set params
    S = Solution()
    S.rows = len( BP.board )-1
    S.cols = len( BP.board[0] )-1
    S.letterDict = BP.letter_dict
    S.board = BP.board
    
    # Find Solutions
    print( f'Words Found: {S.findWordsInBoggle( BP.words )}' )