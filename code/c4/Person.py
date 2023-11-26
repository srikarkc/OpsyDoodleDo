class Person:
    age = 26
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} is {Person.age} years old"

alap = Person("Alap")
edwin = Person("Edwin")

print(alap)
print(edwin)