class product:
    empty=[]
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def set_discount(self,per):
        empty= (per/100)*self.price
        self.price -= empty

    def display(self):
        print({self.name} , {self.price})
productid = [product('i phone', 120000)]
for product in productid:
    product.set_discount(10)
    print(product.display())





