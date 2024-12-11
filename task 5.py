class laptop:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f' {self.brand} , {self.model}')

obj=laptop('HP','PAVILLION')
obj.display()

