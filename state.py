
import chessutil
import string

class State():
    def __init__(self):
        self.board = self.boardinit()
        self.moves = 0
        self.turn = "W"

    def display(self):
        print "Pretty printing board"
        print ""
        print "  {0}  {1} ".format(self.moves, self.turn)
        for index in xrange(25,-5,-5):
            for i in range(index,index+5):
                print self.board[i],
            print ""

    def pieceAt(self, x, y):

        pieceletter = self.board[(y * 5) + x]

        return pieceletter

    def colorAt(self, x, y):

        pieceletter = self.board[(y * 5) + x]
        if pieceletter in string.ascii_lowercase
            color = "B"
        else:
            color = "W"

        return color



    def boardinit(self):
        board = []
        rows = []

        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        
        for row in rows:
            for letter in row:
                board.append(letter)

        return board

    def moveGen(self):
        return generateMoves(self)

         

    
