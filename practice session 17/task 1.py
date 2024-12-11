class animal:
    def print(self):
        print("parent class")
class child(animal):
    def child(self):
        print("child class")

print(issubclass(child,animal))