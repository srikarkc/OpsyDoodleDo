class Person:
    # Static variable
    number_of_people  = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1

    @staticmethod
    def people_count_reset():
        Person.number_of_people = 0

person1 = Person("Hisham", 25)
person1 = Person("Hisham2", 15)
print(Person.number_of_people)

Person.people_count_reset()
print(Person.number_of_people)