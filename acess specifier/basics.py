#THEY DEFINE THE SCOPE OF VARIABLE,CLASS AND
# THREE ACCESSIFIER
# 1.) PRIVATE
# 2.) PUBLIC
# 3.) PROTECTED
from symtable import Class


class Myclass:
    a=10
    def display(self):
        print(self.a)
obj=Myclass()
obj.display()

#PUBLIC ACCESS
# class public:
#     def __init__(self):
#         self.public_var=' i am variable'
#     def public_method(self):
#         print('i am public')

#PRIVATE ACCESS
class private:
    __a = 10         #private
    _a=100           #protected
    def display(self):
            print(self.__a)

#protected access
class protected(private):
    def display(self):
        print(self._a)

obj=protected()
obj.display()


