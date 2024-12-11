# getter setter is used to access the private accessifier
class student:
    def __init__(self,name,age):
        self.__name=name                   #private
        self.__age=age                     #private
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new__name):
        self.__name=new__name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new__age):
        if new__age > 0:
            self.__age=new__age
obj=student('aniket',23)
print(obj.name)
print(obj.age)
obj=student('ansh',24)
print(obj.name)
print(obj.age)