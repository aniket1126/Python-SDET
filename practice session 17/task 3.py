import math
class shape:
    def area(self):
        raise NotImplementedError("non implementing error")


class rectangle(shape):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def area(self):
        return self.l * self.b * self.h


class circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)


shape = [rectangle(2, 3, 4), circle(2)]
for area in shape:
    print(area.area())
