class Car:
    def __init__(self , brand, colour, price):
        self.brand = brand
        self.colour = colour
        self.price = price

obj = Car("Tata","Black",800000)

print(obj.brand)
print(obj.colour)
print(obj.price)
print(type(obj))
print(id(obj))