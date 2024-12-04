#classes
#class is module
#class contains variable and methods
#class will implement
#the variable inside the method is local variable

#class Myclass:
#    def myfun(self):
#        pass
#    def display1(self):
#        print('hello python')
#    def display(self,name,age):
#        print('hello',name,age)

#CREATE AN OBJECT
#obj1=Myclass()
#obj2=Myclass()

#obj1.myfun()
#obj2.display('david',20)

#obj2.myfun()
#obj2.display('scot',23)

#obj1.display1()

#STATIC METHOD  (INSTANCE METHOD IS CALLED USING OBJECTS AND WE CAN CALL DIRECTLY WITH CLASS NAME)
#class Myclass:
#    def m1(self):
#        print('this is instance')
#    @staticmethod
#    def m2(num):
 #       print(num)

#obj1=Myclass()
#obj1.m1()
#obj1.m2(10)
#Myclass.m2(20)

#VARIABLE IN PYTHON
#GLOBAL
#LOCAL -- METHOD VARIABLE
#INSTANCE -- CLASS VARIABLE(SELF)      (self is default argument with variable)
#class Myclass:
#    a,b=10,20
#    def add(self):
#   def multi(self):
#        print(self.a*self.b)

#obj=Myclass()
#obj.add()
#obj.multi()

#ALL VARIABLES
i,j=15,25     #(GLOBAL)

#class Myclass:
#    a,b=10,20
#    def add(self,x,y):
#        print(x,y)
#        print(self.a+self.b)
#    print(i,j)

#mc=Myclass()
#mc.add(10,20)

#USING SAME NAME FOR ALL VARIABLES
i,j=15,25
class Myclass:
    i,j=10,20
    def add(self,i,j):
        print(i,j)
        print(self.i+ self.j)
        print(globals()['i'],globals()['j'])

mc=Myclass()
mc.add(3,4)








































