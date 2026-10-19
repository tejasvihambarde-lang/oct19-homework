class Book:

    def __init__ (self, title, author, price):

        self.title = title
        self.author = author
        self.price = price

obj = Book("python", "john", 500)


print(obj.title)
print(obj.author)
print(obj.price)
print(type(obj))
print(id(obj))