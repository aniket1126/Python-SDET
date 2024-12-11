class product:
    def __init__(self,price,stock):
        self.__price=price
        self.__stock=stock
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,newprice):
        if newprice>0:
            self.__price = newprice
        else:
            print('price can not be negative')

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,newstock):
        if newstock > 0:
            self.__stock=newstock
        else:
            print('stock cant be neagitve')

obj=product(2000,10)
print(obj.price)
print(obj.stock)
obj.price=-23

