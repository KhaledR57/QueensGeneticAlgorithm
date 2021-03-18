#Class NQueenSolver Puzzle Using Backtracking
#
# Author Ahmed Bahaa
# 
# 
class NQueen:
    def __init__ (self, n):
        self.noOfQueens = n
        self.list = [0] * n
        self.numOfSolution = 0
    
    def canPlaceQueen(self, k, i):
        for j in range(k):
            if ( ( self.list[j] == i) or ( abs( self.list[j] - i ) == abs( j - k ) ) ):
                return False

        return True  

    def queenConfiguration(self, k):
        for i in range(self.noOfQueens):
            if( self.canPlaceQueen(k, i) ):
                self.list[k] = i
                if( k == self.noOfQueens - 1):
                    self.printNQueen()
                else:
                    self.queenConfiguration(k + 1)          

    def printNQueen(self):
        self.numOfSolution += 1
        print('the solution  ', self.numOfSolution)
        for i in range(self.noOfQueens):
            for j in range(self.noOfQueens):
                if(i == self.list[j]):
                    print('Q ', end = "")
                else:
                    print("~ ", end = "")
            print("\n")

__8Queens = NQueen(8)
__8Queens.queenConfiguration(0) 
print("The Number Of Solutions of 8 Queen is %d "%__8Queens.numOfSolution )
