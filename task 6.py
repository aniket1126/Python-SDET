import math


class point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def method(self):
        print(math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))



obj = point(3, 7, 4, 1)
obj.method()
