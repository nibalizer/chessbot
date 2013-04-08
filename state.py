#coding: utf-8

import chessutil
import string
import move
import square

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
        """
        zero indexed
        """

        pieceletter = self.board[(y * 5) + x]

        return pieceletter

    def colorAt(self, x, y):

        """
        zero indexed
        """
        pieceletter = self.board[(y * 5) + x]
        if pieceletter in string.ascii_lowercase:
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

    def inBoundsAt(self, x, y):
        bounds = True

        if 0 > x  or x > 4:
            bounds = False

        if 0 > y or y > 5:
            bounds = False

        return bounds

    def moveScan(self,x0,y0,dx,dy,capture=True,stop_short=False):

        """
        To scan from a position x0, y0 in a direction dx, dy
        with optional capture (default true) and with
        optional stop-short (default false):
        """

        """
            x ← x0
            y ← y0
            c ← color of piece at x, y
            moves ← ∅
            repeat
                x ← x + dx
                y ← y + dy
                if x or y is not in bounds
                    break
                if there is a piece p at x, y
                    if the color of p is c
                        break
                    if not capture
                        break
                    stop-short ← true
                insert move from <x0, y0> to <x, y> into moves
            until stop-short
            return moves
        """
        
        x = x0
        y = y0
        c = self.colorAt(x,y)
        #print "color of thing {0}".format(c)
        #print "piece at the place {0}".format(self.pieceAt(x,y))
        moves = []
        #do-while on stop-short
        #print "movescan--init"
        while True:
            x += dx
            y += dy

            if not self.inBoundsAt(x,y):
                #print "Error: out-of-bounds ({0},{1})".format(x,y)
                break

            if self.pieceAt(x,y) != ".":
                #print "Space occuptied ({0},{1}), by {2}".format(x,
                #        y,self.pieceAt(x,y))
                if self.colorAt(x,y) == c:
                    break
                if not capture:
                    break
                stop_short = True

            moves.append(move.Move(square.Square(x0,y0),square.Square(x,y)))
            #print ((x0,y0),(x,y))
            #until/do-while for python
            if stop_short:
                break

        return moves
