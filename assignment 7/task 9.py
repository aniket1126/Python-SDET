class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'Product Name: {self.name}, Price: {self.price}')
        return
product1 = Product("Laptop", 1000)
product1.show()

discounted_price = 700
discount_percentage = 20
original_price = discounted_price / (1 - discount_percentage / 100)
product2 = Product("Smartphone", original_price)
product2.show()
