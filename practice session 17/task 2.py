class person:
    def __init__(self):
        print(' i am person')
    def m1(self):
        print(' i am method from class person')
class employee(person):
    def __init__(self):
        print(' i am constrcutor')
    def m2(self):
        print('i am method from class b')

obj=employee()
obj.m1()
obj.m2()
