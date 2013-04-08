
class Move():
    def __init__(self, from_Square, to_Square,capture):
        self.to_Square = to_Square
        self.from_Square = from_Square
        self.capture = capture
    #def getSquares(self):
    def __str__(self):
        str_rep = "{0}{1}-{2}{3}".format(self.from_Square.x, self.from_Square.y,
                self.to_Square.x, self.to_Square.y)
        return str_rep
    def __eq__(self,othermove):
        return (self.to_Square, self.from_Square) == othermove





