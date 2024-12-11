class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def method(self, per):
        return per / 100 * self.price

productid = [
    Product('iPhone', '67000'),
    Product('LED', '23000'),
    Product('Ferrari Italia', '40000000'),
]

disc_per = 10
for product in productid:
    discount_amount = product.method(disc_per)
    final_price = product.price - discount_amount
    print(f'Product: {product.name}, Original Price: {product.price}, Discounted Price: {final_price}')
