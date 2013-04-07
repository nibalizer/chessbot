#!/usr/bin/env python

import state
import bot


if __name__ == "__main__":
  boardstate = state.State()
  boardstate.display()

  if boardstate.pieceAt(3,2) != '.':
      raise Error("tests no pass")
  if boardstate.pieceAt(1,1) != "P":
      raise Error("tests no pass")
  if boardstate.pieceAt(4,5) != "r":
      raise Error("tests no pass")


