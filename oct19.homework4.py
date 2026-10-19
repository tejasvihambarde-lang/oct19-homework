class Teacher:
    def __init__(self,name,subject,salary):
        self.name = name
        self.subject = subject
        self.salary = salary

obj = Teacher("Atul sir","python",40000)

print(obj.name)
print(obj.subject)
print(obj.salary)
print(type(obj))
print(id(obj))