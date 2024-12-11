#aquring all the attributes & behave methods from one class to another class is called as inheritance
#class a --> a,b,c m1()m2() a is parent of b                 called as (base class/superclass)
#class b --> x,y,z m3()     b is child of class a
from symtable import Class


# SINGLE INHERITANCE (ONE PARENT ONE CHILD)
class A:
   def __init__(self):
       print('i am constructor')
   def m1(self):
       print('i am method from class a')
class B(A):
   def __init__(self):
       print('i am constructor')
   def m2(self):
       print('i am method from class b')
Bobj=B()
Bobj.m1()
Bobj.m2()


#class A:
#    x,y=10,20
#    def m1(self):
#        print(self.x+self.y)
#class B(A):
#    a,b=200,100
#    def m2(self):
#        print(self.a+self.b)
#Bobj=B()
#Bobj.m1()
#Bobj.m2()

#MULTI LEVEL INHERITANCE
#class A:
#    x,y=10,20
#    def m1(self):
#        print(self.x+self.y)
#class B:
#    a,b=2,4
#    def m2(self):
#        print(self.a*self.b)
#class C(B):
#    def m3(self):
#        print(self.a*self.b)

#Cobj=C()
#Cobj.m3()

#HEIRARCHY INHERITANCE
#class A1:
#    a, b = 2, 4
#    def __init__(self):
#           print(" i am construcitr of A1")
#    def m2(self):
#        print(self.a+self.b)
#class A2:
#    i,j=2,4
#    def __init__(self):
#       print(' i am constrcutor of A2')
#    def m3(self):
#        print(self.i+self.j)
#obj=A1
#A1.


#MULTIPLR INHERTIANCE 2 PARENT 1 CHILD
#class A:
#    def print(self):
#        print('this is method from A')

#class B:
#    def print(self):
#        print('this is methof from B')

#class C(B,A):
#    a=10
#    def __init__(self):
#        print(self.a)

#obj=C()
#obj.print()

#METHOD OVERRIDING   PYTHON DOES SUPPORT OVERLOADING BUT WE CAN ACHIEVE FROM DIFFERENT METHODS
# class A:
#     def m1(self):
#         print('this is a method from A')
# class B(A):
#     def m1(self):
#         print('this is method of B')
#         super().m1()                   #invoke immediate parent class parent and variables
#     def print(self):
#         print("hii all")
#
# obj=A()
# obj.m1()

#class A:
#    name='aniket'
# class B(A):
#     def test(self):
#         print(super().name)
# obj=B()
# obj.test()

#OVERRIDING --POLYMORPHISM
# class bank:
#     def roi(self):
#         return 0
# class Xbank(bank):
#     def roi(self):
#         return 10
# class ybank(bank):
#     def roi(self):
#         return 20
#
# obj=Xbank()
# reuslt=obj.roi()
# print(reuslt)
#
# #METHOD OVERLOADING           python does not support directly method overloading
# class admi():
#     def hello(self,name=None):
#         if name is not None:
#             print('hello' + name)
#         else:
#             print('aniket')
# obj=admi()
# obj.hello()cl

# example 2
class cal:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal1=cal()
cal1.add()
cal1.add(2,3)
cal1.add(2,3,4)

