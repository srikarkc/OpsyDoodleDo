# Blueprint for objects
class Person:
    # Attributes - things we know about the object
    def __init__(self, name, age, location, hair_color = "Black"):
        self.name = name
        self.age = age
        self.location = location
        self.hair_color = hair_color
    
    # Method is a function within a class
    def say_hello(self):
        return f"Hello! My name is {self.name}"

# Inheritence
class Indian(Person):
    def __init__(self, name, age, native_state, native_langauge, location = "India"):
        super().__init__(name, age, location)
        self.native_state = native_state
        self.native_language = native_langauge


# Creating an instance of the object
person1 = Person("Alap", 26, "New Westminster")
person2 = Person("Bismi", 25, "Surrey")
person3 = Person("Edwin", 26, "Surrey", "Brown")

person4 = Indian("Ananya Pandey", 25, "Maharastra", "Marathi")
print(person4.name)