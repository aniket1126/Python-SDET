class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement this method")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

shapes = [Square(), Triangle(), Circle()]

for shape in shapes:
    shape.draw()
