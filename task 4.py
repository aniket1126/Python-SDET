class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'name = {self.name} ,age = {self.age}')

obj=person('aniket',23)

obj2=person('ansh',28)
obj3=person('ani',25)
obj.display()
obj2.display()
obj3.display()

