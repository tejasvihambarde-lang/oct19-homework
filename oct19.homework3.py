class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

obj = Mobile("Vivo","Y21",21000)

print(obj.brand)
print(obj.model)
print(obj.price)
print(type(obj))
print(id(obj))