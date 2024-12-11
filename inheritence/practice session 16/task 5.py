class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")

def play_sound(animal: Animal):
    animal.make_sound()


dog = Dog()
cat = Cat()
cow = Cow()


print("Dog sound:")
play_sound(dog)

print("\nCat sound:")
play_sound(cat)

print("\nCow sound:")
play_sound(cow)
