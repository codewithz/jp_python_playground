class Product:

    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        if value<=0:
            raise ValueError('Price cannot be 0 or less')
        self.__price=value;

    def get_price(self):
        return  self.__price;

    def __str__(self):
        return f"Product Name: {self.name} || Price : {self.__price} "

    price= property(get_price,set_price)
#------------------------------------------------------------------

p1=Product('Earphones',300)
p1.set_price(350)
p1.price=-400
print(p1.name,'||',p1.price)
print(p1)
print(p1.price)


# __price    -->  price

