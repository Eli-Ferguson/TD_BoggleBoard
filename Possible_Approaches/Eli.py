import random, string, time
from collections import defaultdict

possibleWords = ["able","acid","ache","acts","aged","ahoy","airy","ajar","akin","alas","ally","alms","also","amid","ammo","amok","ants","aqua","arch","area","army","arts","atom","aunt","avid","away","axes","axis","baby","back","bake","bald","balm","band","bank","bare","bark","base","bash","bath","beak","beam","bean","bear","beat","beef","beer","bees","belt",'word', 'list', 'four', 'play', 'game', 'code', 'time', 'tree', 'park', 'work', 'city', 'book', 'love', 'mind', 'rock', 'team', 'song', 'idea', 'zone', 'baby', 'girl', 'hero', 'data', 'home', 'land', 'help', 'rain', 'road', 'baby', 'ship', 'east', 'west', 'moon', 'fire', 'fish', 'lake', 'sand', 'bird', 'door', 'face', 'hand', 'milk', 'mind', 'star', 'baby', 'idea', 'test', 'trip', 'year', 'cool', 'crap']

n = len( possibleWords )

class Solution :
    def createBoard( self, r, c ) :
        self.board =  [ [ random.choice( string.ascii_lowercase ) for _ in range( c ) ] for _ in range( r ) ]
        self.rows = len( self.board ) - 1
        self.cols = len( self.board[ 0 ] ) - 1

    def createLetterDict( self ) :
        self.lettersDict = defaultdict( list )

        for i in range( len( self.board ) ) :
            for j in range( len( self.board[ 0 ] ) ) :
                letter = self.board[ i ][ j ]
                self.lettersDict[ letter ].append( [ i, j ] )
                
    def findWordsInBoggle( self, words ) :
    
        def DFS( pos, word ) :
            r, c = pos
            
            if self.board[ r ][ c ] == word[ 0 ] :        
                if len( word ) == 1 :
                    # print( f'\tFound')
                    return 1
                
                # up
                if r > 0 and DFS( [ r-1, c ], word[1:] ) : return 1
                # down
                if r < self.rows and DFS( [ r+1, c ], word[1:] ) : return 1
                # left
                if c > 0 and DFS( [ r, c-1 ], word[1:] ) : return 1
                # right
                if c < self.cols and DFS( [ r, c+1 ], word[1:] ) : return 1
                
                # upLeft
                if ( r > 0 and c > 0 ) and DFS( [ r-1, c-1 ], word[1:] ) : return 1
                # upRight
                if ( r > 0 and c < self.cols ) and DFS( [ r-1, c+1 ], word[1:] ) : return 1
                # downLeft
                if ( r < self.rows and c > 0 ) and DFS( [ r+1, c-1 ], word[1:] ) : return 1
                # downRight
                if ( r < self.rows and c < self.cols ) and DFS( [ r+1, c+1 ], word[1:] ) : return 1

                return 0
            
            else :
                return 0
     
        wordsFoundCount = 0
        for word in possibleWords :
        
            # print( f'word: {word}' )
            
            passed = [ letter for letter in word if letter not in self.lettersDict ]
            
            if not passed :
                
                for pos in self.lettersDict[ word[ 0 ] ] :
                    
                    if DFS( pos, word ) :
                        wordsFoundCount += 1
                        break
        
        return wordsFoundCount

for i in range( 5, 20 ) :
    
    startT = time.time()
    
    S = Solution()
    S.createBoard( i, i )
    S.createLetterDict()
    count = S.findWordsInBoggle( possibleWords )
    
    print( f'For Board Size {i}x{i}\nFound {count}/{n} words in {time.time() - startT:.5f} seconds\n')
