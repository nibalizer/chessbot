#coding: utf-8

import chessutil
import string
import move
import square

import math

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
        if pieceletter == '.':
            color = "E"

        return color

    def newBoard(self,rows):
        """
        Create a new board from strings
        """

        board = []

        """
        #create the newboard with something like this
        #NOTE THAT IT IS UPSIDE DOWN
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        """
        
        for row in rows:
            for letter in row:
                board.append(letter)

        self.board = board

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
            capturepiece = False

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

            if self.colorAt(x,y) != c and self.colorAt(x,y) != 'E': 
                capturepiece = True
            moves.append(move.Move(square.Square(x0,y0),square.Square(x,y),
                capturepiece))
            #print ((x0,y0),(x,y))
            #until/do-while for python
            if stop_short:
                break

        return moves

    def moveList(self,x,y):
        """
        To list the moves of a piece at x, y:
        """

        """
        p ← piece at x, y
        moves ← ∅
        switch on type of p
        queen, king:
            for dx in -1 .. 1
                for dy in -1 .. 1
                    if dx = 0 and dy = 0
                        continue
            stop-short ← p = king
            moves ← moves ∪ scan(x, y, dx, dy, stop-short)
            return moves
        rook, bishop:
            dx ← 1
            dy ← 0
            stop-short ← p = bishop
            capture ← p = rook
            for i in 1 .. 4
                moves ← moves ∪ scan(x, y, dx, dy, stop-short, capture)
                exchange dx with dy
                negate dy
            if p = bishop
                dx ← 1
                dy ← 1
                stop-short ← false
                capture ← true
                for i in 1 .. 4
                    moves ← moves ∪ scan(x, y, dx, dy, stop-short, capture)
                    exchange dx with dy
                    negate dy
            return moves
        knight:
            dx ← 1
            dy ← 2
            stop-short ← true
            for i in 1 .. 4
                moves ← moves ∪ scan(x, y, dx, dy, stop-short)
                exchange dx with dy
                negate dy
            dx ← -1
            dy ← 2
            for i in 1 .. 4
                moves ← moves ∪ scan(x, y, dx, dy, stop-short)
                exchange dx with dy
                negate dy
            return moves
        pawn:
            dir ← 1
            if p is black
                dir ← -1
            stop-short ← true
            m ← scan(x, y, -1, dir, stop-short)
            if |m| = 1 and m[0] is a capture
                moves ← moves ∪ m
            m ← scan(x, y, 1, dir, stop-short)
            if |m| = 1 and m[0] is a capture
                moves ← moves ∪ m
            capture ← false
            moves ← moves ∪ scan(x, y, 0, dir, stop-short, capture)
            return moves

        """

        #init
        p = self.pieceAt(x,y)
        moves = []

        #switch on type of p
        #python doesn't have switch/case we just elif like a baws
        
        if p in "kKqQ":
            #Catch kings queens
            #init for king
            stop_short = False
            capture = True
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        #case of no movement
                        continue
                    if p in "kK":
                        #kings move 1 square only
                        stop_short = True
                    moves += self.moveScan(x,y,dx,dy,capture,stop_short)
            return moves

        elif p in "rRbB":
            #catch rooks and bishops
            #init
            dx = 1
            dy = 0
            capture = False
            stop_short = False
            if p in "bB":
                stop_short = True
            if p in "rR":
                capture = True
            for i in range(0,4):
                moves += self.moveScan(x,y,dx,dy,capture,stop_short)
                dx, dy = dy, dx
                dy *= -1
            if p in "bB":
                dx = 1
                dy = 1
                stop_short = False
                capture = True
                for i in range(0,4):
                    moves += self.moveScan(x,y,dx,dy,capture,stop_short)
                    dx, dy = dy, dx
                    dy *= -1

            return moves

        elif p in "nN":
            #catch kNights
            #init
            dx = 1
            dy = 2
            stop_short = True
            capture = True
            for i in range(0,4):
                moves += self.moveScan(x,y,dx,dy,capture,stop_short)
                dx, dy = dy, dx
                dy *= -1
            dx = -1
            dy = 2
            for i in range(0,4):
                moves += self.moveScan(x,y,dx,dy,capture,stop_short)
                dx, dy = dy, dx
                dy *= -1
            return moves

        elif p in "pP":
            #catch pawns
            direction = 1
            if p == 'p':
                direction = -1
            stop_short = True
            capture = True
            m = self.moveScan(x,y,-1,direction,capture,stop_short)
            if len(m) == 1 and m[0].capture: 
                moves += m

            m = self.moveScan(x,y,1,direction,capture,stop_short)
            if len(m) == 1 and m[0].capture: 
                moves += m
            capture = False
            moves += self.moveScan(x,y,0,direction,capture,stop_short)
            return moves





            return moves

        



