import random, string, time
from collections import defaultdict
from functools import cache

# possibleWords = ["able","acid","ache","acts","aged","ahoy","airy","ajar","akin","alas","ally","alms","also","amid","ammo","amok","ants","aqua","arch","area","army","arts","atom","aunt","avid","away","axes","axis","baby","back","bake","bald","balm","band","bank","bare","bark","base","bash","bath","beak","beam","bean","bear","beat","beef","beer","bees","belt",'word', 'list', 'four', 'play', 'game', 'code', 'time', 'tree', 'park', 'work', 'city', 'book', 'love', 'mind', 'rock', 'team', 'song', 'idea', 'zone', 'baby', 'girl', 'hero', 'data', 'home', 'land', 'help', 'rain', 'road', 'baby', 'ship', 'east', 'west', 'moon', 'fire', 'fish', 'lake', 'sand', 'bird', 'door', 'face', 'hand', 'milk', 'mind', 'star', 'baby', 'idea', 'test', 'trip', 'year', 'cool', 'crap', 'aba', 'aca', 'ada', 'aea']

# possibleWords = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

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
    
    def DFS( self, r, c, word ) :
                
        if [ r, c ] in self.traveled :
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

            self.traveled.pop( -1 )
            return 0
        
        else :
            self.traveled.pop( -1 )
            return 0
           
    def findWordsInBoggle( self, words ) :     
     
        wordsFoundCount = 0
        for word in words :
                    
            passed = [ letter for letter in word if letter not in self.lettersDict ]
            
            if not passed :
                
                b = False
                
                for pos in self.lettersDict[ word[ 0 ] ] :
                    
                    self.traveled = []
                    
                    if self.DFS( pos[ 0 ], pos[ 1 ], word ) :
                        # print( f'Found: {word} @ {pos} with {self.traveled}' )
                        wordsFoundCount += 1
                        b = True
                        break
                
                if not b : print( f'Not Found: {word}' )
        
        return wordsFoundCount
    
possibleWords = []

with open("./Possible_Approaches/words.txt") as f:
    for line in f:
        possibleWords.append(line.strip())

n = len( possibleWords )

print()

def from_N_to_M( rangeMin, rangeMax ) :
    timeStart = time.time()
    repeatEach = 1
    for i in range( rangeMin, rangeMax+1 ) :
        
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
                print( f'For Board Size {i}x{i}\nFound {count}/{n} words in {time.time() - startT:.5f} seconds\n')

    print( f'Boards for size {rangeMin}..{rangeMax} done {repeatEach}x times using {n} words completed in {time.time() - timeStart:.5f} seconds')

# from_N_to_M( 5, 100 )

def gridSizes( sizes ) :
    
    timeStart = time.time()
    
    repeatEach = 1
    
    for i in sizes :
        
        startT = time.time()
        
        S = Solution()
        S.createBoard( i, i )
        if i < 20 :
            [ print( row ) for row in S.board ]
            print()
        
        S.createLetterDict()
        # [ print( item ) for item in S.lettersDict.items() ]
        # print()
        
        count = S.findWordsInBoggle( possibleWords )
        
        if count :
            print( f'For Board Size {i}x{i} with {i**2} spots\nFound {count}/{n} words in {time.time() - startT:.5f} seconds\n')

# gridSizes( [ 10 ] )


def test_case() :
    
    Words = [
        'waited', 'wait', 'bin', 'devoid', 'el', 'lo', 'voter', 'hen', 'fled', 'forums', 'mired', 'pure', 'ewe', 'me', 'dug', 'wizard', 'zigs', 'quad', 'quay', 'and', 'yo', 'up', 'magic', 'pitny', 'ons', 'irks', 'tablets', 'lax', 'thee', 'pass', 'toon', 'jets', 'jive', 'corals',
    ]
    
    Board = [
        '   waited     c',
        '   a    el h  o',
        '  bin   voter r',
        '   t    o  n  a',
        '        i     l',
        ' p   fled  jets',
        ' u   o     i o ',
        ' r mired   v op',
        ' ewe u up  e na',
        '  i  magic    s',
        '  zigs  tablets',
        'quad    n  a h ',
        'u r     yo x e ',
        'and      n   e ',
        'yo    irks     '
    ]
    
    S = Solution()
    S.board = Board
    S.rows = len( Board )-1
    S.cols = len( Board[ 0 ] )-1
    
    S.createLetterDict()
    
    count = S.findWordsInBoggle( Words )
    
    assert count == len( Words ), 'Not All Words Found'
    print( f'{count}/{len( Words )} Words Found')
    print( f'Adding: xxxx')
    
    Words.append('xxxx')
    assert count == len( Words )-1, 'Found Non Existent Word'
    print( f'{count}/{len( Words )} Words Found')

test_case()