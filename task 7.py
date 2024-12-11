class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
        print(f' {name} , {salary}')

    def give_raise(self,per):
        self.salary += per/100 * self.salary
        print(f' {self.name} , {self.salary}')



obj=employee(12,'aniket',30000)
obj.give_raise(10)

