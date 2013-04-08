
class Move():
    def __init__(self, from_Square, to_Square):
        self.to_Square = to_Square
        self.from_Square = from_Square
    #def getSquares(self):
    def __str__(self):
        str_rep = "{0}{1}-{2}{3}".format(self.from_Square.x, self.from_Square.y,
                self.to_Square.x, self.to_Square.y)
        return str_rep


