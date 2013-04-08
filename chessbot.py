#!/usr/bin/env python
#coding: utf-8

import state
import bot
import chessutil
import sys


tests = False

try:
    if sys.argv[1] == '-t':
        tests = True
except IndexError:
    pass


if __name__ == "__main__":
  boardstate = state.State()
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
      if " ".join(map(str,things))  == "12-11 13-11 14-11":
      print ".",
      print ""
      print "All tests pass, woot!"
  

