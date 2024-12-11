class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f' name: {self.name}')
        print(f' age: {self.age}')
class emp(person):
    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)
        self.empid=empid
        self.salary=salary
    def display(self):
        super().display()
        print(f"Employee ID: {self.empid}")
        print(f"Salary: {self.salary}")

obj=emp('aniket',23,121,2000000)
obj.display()
