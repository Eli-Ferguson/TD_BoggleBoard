import random, string, time
from collections import defaultdict
from functools import cache

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
    
    # @cache
    def DFS( self, r, c, word ) :
        
        if [ r, c ] in self.traveled :
            # print('CROSSOVER')
            # print( self.traveled )
            return 0
        else :
            self.traveled.append( [ r, c ] )
        
        if self.board[ r ][ c ] == word[ 0 ] :        
            if len( word ) == 1 :
                return 1
            
            # up
            if r > 0 and self.DFS( r-1, c, word[1:] ) : return 1
            # down
            if r < self.rows and self.DFS( r+1, c, word[1:] ) : return 1
            # left
            if c > 0 and self.DFS( r, c-1, word[1:] ) : return 1
            # right
            if c < self.cols and self.DFS( r, c+1, word[1:] ) : return 1
            
            # upLeft
            if ( r > 0 and c > 0 ) and self.DFS( r-1, c-1, word[1:] ) : return 1
            # upRight
            if ( r > 0 and c < self.cols ) and self.DFS( r-1, c+1, word[1:] ) : return 1
            # downLeft
            if ( r < self.rows and c > 0 ) and self.DFS( r+1, c-1, word[1:] ) : return 1
            # downRight
            if ( r < self.rows and c < self.cols ) and self.DFS( r+1, c+1, word[1:] ) : return 1

            return 0
        
        else :
            return 0
           
    def findWordsInBoggle( self, words ) :     
     
        wordsFoundCount = 0
        for word in possibleWords :
                    
            passed = [ letter for letter in word if letter not in self.lettersDict ]
            
            if not passed :
                
                for pos in self.lettersDict[ word[ 0 ] ] :
                    
                    self.traveled = []
                    
                    if self.DFS( pos[ 0 ], pos[ 1 ], word ) :
                        # print( f'Found: {word} @ {pos} with {self.traveled}' )
                        wordsFoundCount += 1
                        break
        
        return wordsFoundCount

print()
timeStart = time.time()
rangeMin = 5
rangeMax = 100
repeatEach = 5
for i in range( rangeMin, rangeMax ) :
    
    for _ in range( repeatEach ) :
        startT = time.time()
        
        S = Solution()
        S.createBoard( i, i )
        # [ print( row ) for row in S.board ]
        # print()
        
        S.createLetterDict()
        # [ print( item ) for item in S.lettersDict.items() ]
        # print()
        
        count = S.findWordsInBoggle( possibleWords )
        
        if count :
            # [ print( row ) for row in S.board ]
            # print()
            print( f'For Board Size {i}x{i}\nFound {count}/{n} words in {time.time() - startT:.5f} seconds\n')

print( f'Boards for size {rangeMin}..{rangeMax} done {repeatEach}x times using {n} words completed in {time.time() - timeStart} seconds')
