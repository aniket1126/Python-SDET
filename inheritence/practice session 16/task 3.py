class animal:
    def make_sound(self):
        raise NotImplementedError('not included')

class dog(animal):
    def make_sound(self):
        print('bhoww')
class cat(animal):
    def make_sound(self):
        print('meahuu')
class cow(animal):
    def make_sound(self):
        print('ohhh')

animals=[dog(),cat(),cow()]
for animal in animals:
    animal.make_sound()


