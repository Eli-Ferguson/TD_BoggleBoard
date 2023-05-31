import sys

from problem import BoggleProblem
from Solver import Solution

if __name__ == '__main__' :
    # Get File Paths From Args
    BoardsFile, wordsFile = sys.argv[ 1 ], sys.argv[ 2 ]
        
    # Read Boards and Words From Files
    BP = BoggleProblem( words_file=wordsFile, board_file=BoardsFile )
    
    # Create and set params
    S = Solution( board=BP.board, letterDict=BP.letter_dict )
    
    # Find Solutions
    print( f'Words Found: {S.findWordsInBoggle( BP.words )}' )