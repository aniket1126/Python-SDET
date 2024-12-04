#constructors in python
#constructor name is fixed def __init__(self)
#it will not return any value
#it also receives arguments/parameters
#it will be called automatically at the time of object creation
#constructor is used to create and initialze the object
from itertools import permutations


#class Myclass:
#    def __init__(self):
#        print('i am constructor of the class')
#    def m1(self):
#        print('hello i am method')

#obj1=Myclass()
#obj1.m1()

#class Myclass:
#    def __init__(self):
#        print('i am constructor of the class')
#    def m1(self):
#        print(self)

#    def m2(self,a,b):
#        return a+b


#obj1=Myclass()
#obj1.m1()
#obj1.m2(12,20)

#PARAMETERIZED CONSTRUCTOR
class Myclass:

    def __init__(self):
        name = 'david'
        print(name)
       # print(self.name)
    #def show(self):
# print(self.name)
#obj=Myclass()
#obj.show()

#
#class employee:
#    def __init__(self,eid,ename,esal):
#        self.eid=eid
#        self.ename = ename
#        self.esal = esal
#    def display(self):
#        print(self.eid,self.ename,self.esal)

#obj1 = employee('102','aniket',40000)
#obj1.display()

#__str__ CONSTRUCTOR
#class Myclass:
#    def __str__(self):
#        return 'hello i am method'

#obj1=Myclass()
#print(obj1)

#DELETE OBJ PROPERTIES IN PYTHON --DEL
#WE CAN DELETE THE OBJ PROPERTIES (ALSO CALLED THE ATTRIBUTE )USING DEL STATEMENT

#class car:
#    def __init__(self,brand,model):
#        self.brand=brand
#        self.model=model

#    def __str__(self):
#        return f"brand: { self.brand}, model: {self.model}"

#c=car('tata','nexon')
#print(c.brand)
#print(c.model)
#print(c)

#del c.brand
#print(c.brand)    AttributeError: 'car' object has no attribute 'brand'

#
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age


person1 = Person()









