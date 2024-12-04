class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f"brand: { self.brand}, model: {self.model}"

c=car('tata','nexon')
print(c.brand)
print(c.model)
print(c)

del c.brand
print(c.brand)