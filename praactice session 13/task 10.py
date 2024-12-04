class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append({"item": item})
        print(f'{item} added to cart')

    def remove(self, item):
        for cart_item in self.cart:
            if cart_item['item'] == item:
                self.cart.remove(cart_item)
                print(f'{item} is removed from the cart')

        print(f'{item} is not found in the cart')

    def display(self):
        for cart_item in self.cart:
            print(f"{cart_item['item']}")


cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("banana")
cart.display()

cart.remove('apple')
cart.display()
