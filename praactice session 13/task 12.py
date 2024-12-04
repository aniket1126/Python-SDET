class circle:
    def __init__(self,l,b,h,pi,r):
        self.l=l
        self.b=b
        self.h=h
        self.pi=pi
        self.r=r

    def display(self):
        print((self.l)*(self.b)*(self.h))
        print(2*(self.pi)*(self.r))

obj1=circle(2,3,1,3.14,2)
obj1.display()

