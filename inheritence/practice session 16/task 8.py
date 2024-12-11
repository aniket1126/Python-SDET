class Transport:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Airplane(Transport):
    def move(self):
        print("The airplane is flying")





class Ship(Transport):
    def move(self):
        print("The ship is sailing.")

class Car(Transport):
    def move(self):
        print("The car is driving ")

transport_list = [Airplane(), Ship(), Car()]

for transport in transport_list:
    transport.move()
