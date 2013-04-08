#!/usr/bin/env python
#coding: utf-8

import bot
import chessutil
import move
import square
import state

import sys


tests = False

try:
    if sys.argv[1] == '-t':
        tests = True
except IndexError:
    pass


if __name__ == "__main__":
    boardstate = state.State()
    if not tests:
        boardstate.display()


    if tests:
        print "Running tests"
        if boardstate.pieceAt(3,2) != '.':
            raise Error("tests no pass")
        print ".",
        if boardstate.pieceAt(1,1) != "P":
            raise Error("tests no pass")
        print ".",
        if boardstate.pieceAt(4,5) != "r":
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(3,3)  !=  True:
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(1,1)  !=  True:
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(-1,1) !=  False:   
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(1,-1) !=  False:    
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(6,1)  !=  False:         
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(1,6)  !=  False:   
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(6,7)  !=  False:
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(8,6)  !=  False:
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(-1,-1) != False:
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(-1,-1) != False: 
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(0,0)   != True: 
            raise Error("tests no pass")
        print ".",
        if boardstate.inBoundsAt(4,5)   != True:
            raise Error("tests no pass")
        things = boardstate.moveScan(1,1,0,1)
        if " ".join(map(str,things))  !=  "11-12 11-13 11-14":
            #print " ".join(map(str,things))
            raise Error("tests no pass")
  
        print ".",
        bottomrow = ""
        bottomrow += boardstate.pieceAt(0,0)
        bottomrow += boardstate.pieceAt(1,0)
        bottomrow += boardstate.pieceAt(2,0)
        bottomrow += boardstate.pieceAt(3,0) 
        bottomrow += boardstate.pieceAt(4,0) 
        if bottomrow != "RNBQK":
            #print bottomrow
            raise Error("tests no pass")
  
        print ".",
        toprow = ""
        toprow += boardstate.pieceAt(0,5)
        toprow += boardstate.pieceAt(1,5)
        toprow += boardstate.pieceAt(2,5)
        toprow += boardstate.pieceAt(3,5) 
        toprow += boardstate.pieceAt(4,5) 
        if toprow != "kqbnr":
            raise Error("tests no pass")
  
  
        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        boardstate.newBoard(rows)
  
  
  
        print ".",
        #these two tests are run again after newboard
        bottomrow = ""
        bottomrow += boardstate.pieceAt(0,0)
        bottomrow += boardstate.pieceAt(1,0)
        bottomrow += boardstate.pieceAt(2,0)
        bottomrow += boardstate.pieceAt(3,0) 
        bottomrow += boardstate.pieceAt(4,0) 
        if bottomrow != "RNBQK":
            #print bottomrow
            raise Error("tests no pass")
  
        print ".",
        toprow = ""
        toprow += boardstate.pieceAt(0,5)
        toprow += boardstate.pieceAt(1,5)
        toprow += boardstate.pieceAt(2,5)
        toprow += boardstate.pieceAt(3,5) 
        toprow += boardstate.pieceAt(4,5) 
        if toprow != "kqbnr":
            raise Error("tests no pass")
  
        print ".",
        #create the newboard with something like this
        rows = []
        rows.append(".N.QK")
        rows.append(".qB.P")
        rows.append("R..P.")
        rows.append("...p.")
        rows.append("p.p..")
        rows.append("k.bnr")
        boardstate.newBoard(rows)
        #boardstate.display()
  
        print ".",
        #these two tests are run again after newboard
        bottomrow = ""
        bottomrow += boardstate.pieceAt(0,0)
        bottomrow += boardstate.pieceAt(1,0)
        bottomrow += boardstate.pieceAt(2,0)
        bottomrow += boardstate.pieceAt(3,0) 
        bottomrow += boardstate.pieceAt(4,0) 
        if bottomrow != ".N.QK":
            #print bottomrow
            raise Error("tests no pass")
  
        print ".",
        toprow = ""
        toprow += boardstate.pieceAt(0,5)
        toprow += boardstate.pieceAt(1,5)
        toprow += boardstate.pieceAt(2,5)
        toprow += boardstate.pieceAt(3,5) 
        toprow += boardstate.pieceAt(4,5) 
        if toprow != "k.bnr":
            raise Error("tests no pass")
  
  
        print ".",
        #test movescan for queens and kings
        moves = boardstate.moveScan(1,1,0,1)
        if " ".join(map(str,moves))  !=  "11-12 11-13 11-14 11-15":
            print " ".join(map(str,moves))
            raise Error("tests no pass")
  
        
        #test all directions on the queen for the new board
        dxy = [ (1,1,'11-22'),
                (1,0,'11-21'),
                (1,-1,'11-20'),
                (0,1,'11-12 11-13 11-14 11-15'),
                (0,-1,'11-10'),
                (-1,1,'11-02'),
                (-1,0,'11-01'),
                (-1,-1,'11-00')
                ]

        for dirs in dxy:

            print ".",
            dx,dy,results = dirs
            #test movescan
            #print "moving in direction {0},{1}".format(dx,dy)
            #print "resulting moves: {0}".format(results)
            moves = boardstate.moveScan(1,1,dx,dy)
            if " ".join(map(str,moves))  !=  results:
                try: 
                    raise Error("tests no pass")
                except NameError:
                    boardstate.display()
                    print " ".join(map(str,moves))
                    raise Error("tests no pass")
  
        print ".",
        #test movelist for queens and kings
        #black queen
        moves = boardstate.moveList(1,1)
        if " ".join(map(str,moves))  !=  "11-00 11-01 11-02 11-10 11-12 11-13\
 11-14 11-15 11-20 11-21 11-22":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

  
        print ".",
        #test movelist for queens and kings
        #black king
        moves = boardstate.moveList(0,5)
        if " ".join(map(str,moves))  !=  "05-14 05-15":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))
  
        print ".",
        #test movelist for queens and kings
        #white queen
        moves = boardstate.moveList(3,0)
        if " ".join(map(str,moves))  !=  "30-20 30-31":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for queens and kings
        #white king
        moves = boardstate.moveList(4,0)
        if " ".join(map(str,moves))  !=  "40-31":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for bishop
        #white bishop
        moves = boardstate.moveList(2,1)
        if " ".join(map(str,moves))  !=  "21-31 21-20 21-22 21-12 21-03":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for bishop
        #black bishop
        moves = boardstate.moveList(2,5)
        if " ".join(map(str,moves))  !=  "25-15 25-34 25-43 25-14 25-03":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for rook
        #white rook
        moves = boardstate.moveList(0,2)
        if " ".join(map(str,moves))  !=  "02-12 02-22 02-01 02-00 02-03 02-04":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for rook
        #black rook
        moves = boardstate.moveList(4,5)
        if " ".join(map(str,moves))  !=  "45-44 45-43 45-42 45-41":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))


        print ".",
        #test movelist for knight
        #black knight
        moves = boardstate.moveList(3,5)
        if " ".join(map(str,moves))  !=  "35-23 35-43 35-14":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for knight
        #black knight
        moves = boardstate.moveList(1,0)
        if " ".join(map(str,moves))  !=  "10-22 10-31":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for pawn
        #white pawn
        moves = boardstate.moveList(3,2)
        if " ".join(map(str,moves))  !=  "":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for pawn
        #black pawn
        moves = boardstate.moveList(2,4)
        if " ".join(map(str,moves))  !=  "24-23":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #create the newboard with something like this
        rows = []
        rows.append(".N.QK")
        rows.append(".qB.P")
        rows.append("R..PP")
        rows.append("..pp.")
        rows.append("p.p..")
        rows.append("k.bnr")
        boardstate.newBoard(rows)
        #boardstate.display()

        print ".",
        #test movelist for pawn
        #white pawn
        moves = boardstate.moveList(3,2)
        if " ".join(map(str,moves))  !=  "32-23":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #test movelist for pawn
        #black pawn
        moves = boardstate.moveList(2,3)
        if " ".join(map(str,moves))  !=  "23-32 23-22":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + " ".join(map(str,moves)))

        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        boardstate.newBoard(rows)

        print ".",
        mymove = move.Move(square.Square(1,1),square.Square(1,2),False)
        boardstate.move(mymove)
        if boardstate.pieceAt(1,2) != "P":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + boardstate.pieceAt(1,2))
        print ".",
        if boardstate.pieceAt(1,1) != ".":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + boardstate.pieceAt(1,2))

        print ".",
        boardstate.humanMove("b5-b4")
        if boardstate.pieceAt(1,3) != "p":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + boardstate.pieceAt(1,2))
        print ".",
        if boardstate.pieceAt(1,4) != ".":
            print ""
            boardstate.display()
            raise NameError("tests no pass: " + boardstate.pieceAt(1,2))
        
        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append(".qbnr")
        boardstate.newBoard(rows)

        print ".",
        if boardstate.gameOver() != True:
            print ""
            boardstate.display()
            raise NameError("tests no pass: game should be over" )

        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQ.")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        boardstate.newBoard(rows)

        print ".",
        if boardstate.gameOver() != True:
            print ""
            boardstate.display()
            raise NameError("tests no pass: game should be over" )

        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        boardstate.newBoard(rows)
        boardstate.rounds = 40
        boardstate.turn = "W"

        print ".",
        if boardstate.gameOver() != True:
            print ""
            boardstate.display()
            raise NameError("tests no pass: game should be over" )

        print ".",
        #create the newboard with something like this
        rows = []
        rows.append("RNBQK")
        rows.append("PPPPP")
        rows.append(".....")
        rows.append(".....")
        rows.append("ppppp")
        rows.append("kqbnr")
        boardstate.newBoard(rows)
        boardstate.rounds = 19 
        boardstate.turn = "W"
  
        print ".",
        if boardstate.gameOver() != False:
            print ""
            boardstate.display()
            raise NameError("tests no pass: game should not be over" )


        print ".",
        print ""
        print "All tests pass, woot!"
        boardstate.display()

