import random, string, time
from collections import defaultdict

possibleWords = [ 'a', 'ab', 'bc', 'abc' ]

rows, cols = 20, 20

boggleBoard = [ [ random.choice( string.ascii_lowercase ) for _ in range( cols ) ] for _ in range( rows ) ]

rows -= 1
cols -= 1

[ print( row ) for row in boggleBoard ]
print()

lettersFound = defaultdict( list )

for i in range( rows ) :
    for j in range( cols ) :
        letter = boggleBoard[ i ][ j ]
        lettersFound[ letter ].append( [ i, j ] )

[ print( item ) for item in lettersFound.items() ]
print()

def DFS( pos, word ) :
        
    r, c = pos
    
    # print( pos, boggleBoard[ r ][ c ], word )
    
    if boggleBoard[ r ][ c ] == word[ 0 ] :        
        if len( word ) == 1 :
            print( f'\tFound')
            return 1
        
        # up
        if r > 0 and DFS( [ r-1, c ], word[1:] ) : return 1
        # down
        if r < rows and DFS( [ r+1, c ], word[1:] ) : return 1
        # left
        if c > 0 and DFS( [ r, c-1 ], word[1:] ) : return 1
        # right
        if c < cols and DFS( [ r, c+1 ], word[1:] ) : return 1
        
        # upLeft
        if ( r > 0 and c > 0 ) and DFS( [ r-1, c-1 ], word[1:] ) : return 1
        # upRight
        if ( r > 0 and c , cols ) and DFS( [ r-1, c+1 ], word[1:] ) : return 1
        # downLeft
        if ( r < rows and c > 0 ) and DFS( [ r+1, c-1 ], word[1:] ) : return 1
        # downRight
        if ( r < rows and c < cols ) and DFS( [ r+1, c+1 ], word[1:] ) : return 1

        return 0
    
    else :
        return 0

wordsFoundCount = 0

startT = time.time()

for word in possibleWords :
    
    print( f'word: {word}' )
    
    passed = [ letter for letter in word if letter not in lettersFound ]
    
    if not passed :
        
        for pos in lettersFound[ word[ 0 ] ] :
            
            if DFS( pos, word ) :
                wordsFoundCount += 1
                break

print( f'Found {wordsFoundCount} words in {time.time() - startT:.5f} seconds' )