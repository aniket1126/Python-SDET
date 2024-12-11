class car:
    wheel=4
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        print(self.brand)
        print(self.wheel)
obj=car('volvo')
obj.show()

obj=car('audi')
obj.show()