
class Square():
    def __init__(self, x, y):
        if x not in range(5):
            raise ValueError("x coordinate not in range")
        if y not in range(6):
            raise ValueError("x coordinate not in range")
        self.x = x
        self.y = y


