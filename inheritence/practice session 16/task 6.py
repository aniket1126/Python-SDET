class Appliance:
    def turn_on(self):
        raise NotImplementedError("Subclass must implement this method")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now running.")

class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now cooling.")

class Microwave(Appliance):
    def turn_on(self):
        print("Microwave is now heating.")


appliances = [WashingMachine(), Refrigerator(), Microwave()]
for appliance in appliances:
    appliance.turn_on()
