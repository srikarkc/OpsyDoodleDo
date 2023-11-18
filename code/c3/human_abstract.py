from abc import ABC, abstractmethod

# Creating an abstract class that cannot be instantiated
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def greet(self):
        pass

    def walk(self):
        return "Moved forward by 1 step."
        

class Indian(Person):
    def __init__(self, name, age, native_state):
        super().__init__(name, age)
        self.native_state = native_state
    
    def greet(self):
        return f"Namaste!"
    
    # overridden method
    def walk(self):
        return "Moved forward by 1 step on the road."

class Canadian(Person):
    def __init__(self, name, age, native_province):
        super().__init__(name, age)
        self.native_state = native_province

    def greet(self):
        return f"Wassup!"
    
    # overridden method
    def walk(self):
        return "Moved forward by 1 step on the sidewalk."
    
person1 = Canadian("Kyle", 17, "BC")
person2 = Indian("Gayathri", 26, "Kerala")

print(person1.walk())
print(person2.walk())