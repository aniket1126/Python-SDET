class car1:
    brand,model = "",""
    def carinfo(self,brand,model):
        print(brand,model)

obj1 = car1()
obj2 = car1()
obj3 = car1()

obj1.carinfo("swift",2015)
obj2.carinfo("verna",2017)
obj3.carinfo("scorpio",2013)
