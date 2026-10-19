class Animal:
    def __init__(self, name, colour, sound):
        self.name = name
        self.colour = colour
        self.sound = sound

obj = Animal("dog","black", "bark")

print(obj.name)
print(obj.colour)
print(obj.sound)
print(type(obj))
print(id(obj))
        

