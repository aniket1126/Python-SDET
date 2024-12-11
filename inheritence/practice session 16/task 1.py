class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class car(vehicle):
    def __init__(self, num_doors, brand, model):
        super().__init__(brand, model)
        self.num_doors = num_doors
    def display(self):
        print(f' brand: {self.brand}, model of car: {self.model}, no of doors: {self.num_doors}')

obj=car(5,'volvo',2012)
obj.display()
