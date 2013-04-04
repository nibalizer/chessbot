
class State():
    def __init__(self):
        self.board = self.boardinit()
        self.moves = 0
        self.turn = "W"

    def display(self):
        print "Pretty printing board"
        print ""
        print "  {0}  {1} ".format(self.moves, self.turn)
        for index in xrange(0,30,5):
            for i in range(index,index+5):
                print self.board[i],
            print ""


    def boardinit(self):
        board = []
        rows = []

        rows.append("kqbnr")
        rows.append("ppppp")
        rows.append(".....")
        rows.append(".....")
        rows.append("PPPPP")
        rows.append("RNBQK")
        
        for row in rows:
            for letter in row:
                board.append(letter)

        return board
         

    
