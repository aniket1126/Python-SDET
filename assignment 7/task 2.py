class counter:
    count = 0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        counter.count += 1
    def person(self):
        print(f' my name is {self.name} and my age is {self.age}')


obj1 = counter('Aniket', 23)
obj2 = counter('John', 30)
obj1.person()
obj2.person()
print(f'total number of obj created are {counter.count}')
