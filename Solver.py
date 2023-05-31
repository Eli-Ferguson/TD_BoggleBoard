from collections import defaultdict

class Solution :
    
    rows = 0
    cols = 0
    letterDict = {}
    board = [[]]
    
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