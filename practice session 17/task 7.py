class vehicle:
    def display(self):
        pass

class car(vehicle):
    def display(self):
        print('car engine is started')
class bike(vehicle):
    def display(self):
        print('bike engine is started')

vehicle=[car(),bike()]
for vehicles in vehicle:
    vehicles.display()
