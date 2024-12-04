class rectangle:
    def calculate(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def display(self):
        print((self.l)*(self.b)*(self.h))

obj=rectangle()
obj.calculate(2,3,1)
obj.display()