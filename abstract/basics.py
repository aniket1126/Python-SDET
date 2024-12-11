#ABSTRACTION CLASSES that contains method and methods
#they serve as a blueprint for other classes

from abc import ABC, abstractmethod

from pracitce_programs.task20 import value1, value2


#EXAMPLE 1 FOR ABSTRACT CLASS
# class A(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     def display2(self):
#         print(' i am display method')
# class B(A):
#     def display(self):
#         print('i am concrete of b')
#     def display1(self):
#         print('i am display method of b(A)')
#
# class C(B):
#     def display(self):
#         print('hii')
#     def name(self):
#         print(' i am aniket')
#
# obj=C()
# obj.display()
# obj.display2()

#EXAPMLE 2
# class cal(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     pass
# class result(cal):
#     def add(self):
#         print(self.value+100)
#     def sub(self):
#         print(self.value_100)
# R=result()
# R.add()
# R.sub()

class shape(ABC):
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
@abstractmethod
def area(self):
    pass
@abstractmethod
def para(self):
    pass
class rectangle(shape):
    def area(self):
        print(self.val1*self.val2)
    def para(self):
        print(2*self.val1+self.val2)

obj=rectangle(2,5)
obj.area()
obj.para()

















































