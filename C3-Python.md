# Class 3 - November 18, 2024 - Linux

## Introduction
![Python Banner](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)

> Python is the greatest programming language of all time.

---

## What is programming?

> Set of instructions to communicate w/ the hardware.

> We write source code to perform certain actions.

Each character is mapped to a number that can be represented in binary.

In order to provide instructions to a computer, we need to convert human readable instructions into binary. So, each alphabet is mapped to a number. This convention is represented in ASCII.

![ASCII Table](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/875px-ASCII-Table-wide.svg.png)


## What are the common programming languages and pradigms?

Python, Java, C, C++, C#, R, Ruby, Go, Cobol, Fortran, PHP, PowerShell, BASH, JavaScript, Batch, VBA, .NET, Terraform, AWS CLI, Rust, Puppet, Kotlin, Fluttr, Dart, Sonic Pi

![Programming Language Classification](https://danluu.com/images/empirical-pl/lang_classes.png)

### Programming Paradigms

Procedural -> Step by step. If one step breaks, the program stops.
Script -> Set of instructions to automate tasks.
Functional -> Possible to skip function run in case of error.

Each language used in different scenarios or some languages improve upon others.

Some languages are easier.

### Dynamically typed vs Statically typed

Dynamically typed -> Python. No compilation before running. You have an interpreter. 

If you're running a dynamically typed lanaguage, you need to have the same version interpreter installed.

What is the difference between a library and a module?
Module -> Set of code of functions.
Library -> Collection of modules or packages.

Statically typed -> Java. Source Code -> Compile to byte code -> Run in a JVM.

No need for Interpreter or JDK. You will need JRE still to create JVM to run.

### Strongly typed vs Weakly typed

In a strongly typed programming language, the type of a variable is enforced and checked at compile-time or runtime.
In a weakly typed programming language, the type of a variable is more flexible and can change at runtime.


### High level & Low level

High level understood by humans. Close to humans.

Low level is closer to what is understood by machines.


### Memory Class

Java has a Garbage Collector (GC) that removes objects from the Heap when there are no longer any Reference Variables pointing to it.
2 memory locations -> Stack and Heap
Memory Leak -> When Heap runs out of space.

---

# Python programming

### VS Code Installed

### Python Basics

1. Defined variables -> Float, Integer, & String

```
  piston_diameter = 74.50 
  piston_count = 4
  engine_type = "Inline"
  stroke_length = 80
```

2. Defined a function

```
def calculate_piston_volume(diameter, stroke_lenth):
    radius = diameter / 2
    stroke_area = math.pi * (radius**2)
    return stroke_area * stroke_length
```

3. Control Flow

```
if total_volume > 1500:
    category = "large"
elif total_volume > 1000:
    category = "medium"
else:
    category = "small"
```


4. Collection data types

List -> Ordered mutable collection. You can perform slice, add, remove etc. Can have duplicated value. '[]' are used for List. 
Tuple -> Ordered immutable collection. Can have duplicated value. '()' used for Tuple
Set - > Unordered mutable collection. You can perform add and remove. Can't have duplicates. set() used to create set.

5. For loop

```
for machine in machines:
    # Unpacking Tuple
    machine_id, task = machine
    print(f"Performing {task} on {machine_id}.")
    completed_maintenance.add(machine_id)
```

6. While loop

```
parts_used = ["Oil", "Filter", "Belt", "Oil", "Belt"]
parts_inventory = {}

while parts_used:
    part = parts_used.pop()
    if part in parts_inventory:
        parts_inventory[part] += 1
    else:
        parts_inventory[part] = 1
```

Difference between for loop and while loop ->

You use for loop when you know the number of elements.
You use while loop when you don't know the number of elements.


7. Functions and modules

Function: A function is a block of organized reusable code. 
Module: A module a collection of functions. 
Import a module -> `import <module_name>` -> To use in source code -> `<module_name>.<function_name>`
Import all functions from a file -> `from <module_name> import *` -> You can refer to the functions by their name.


```
def calculate_stress(force, area = 500):
    '''
        Takes in a force and area and returns stress.
    '''
    stress = force / area
    return stress
```
Here, we defined a default value for area. So, you don't have to pass an argument for area parameter.

```
print(calculate_stress(50))
```

#### Types of arguments


Positional Arguements: In positional arguments, you'd pass arguments relating to the position of the parameter within the function.

```
print(calculate_stress(50, 1000))
```

Keyword Arguments: In these arguments, you'd pass the arguments by specifying the keyword. So, the order doesn't matter.
 
```
print(calculate_stress(area=100, force=50))
```
Variables number of arguments: By defining the pressure parameter, we can pass as many arguments as needed. However, we'd need to pass a keyword argument for area here.

```
def calculate_total_force(*pressures, area = 500):
    total_force = sum(pressures) * area
    return total_force

+
  nt(calculate_total_force(10, 20, 30, area = 2000))

```

Lambda Functions (aka anonymous functions): it is used for small and temporary functions. For instance, in the example below, rather than using a two line code to get the X to the power of Y, we use lambda. 

```
square = lambda x,y: x**y

print(f"{square(5,2)}")
```

---

## Object Oriented programming

Attributes and methods

Attributes - Things we know about the Object
Method - Things the object can do

1. We created a blueprint - Class

2. We instantiated the class by creating 'person1' object

3. We saw that objects are stored on the Heap at different virtual memory addresses.

```
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
```

### Inheritence

We created an 'Indian' subclass which inherited from 'Person' subclass.

We added the super's attributes to the sub-class by passing the argument to the method and also to super().__init__

```
class Indian(Person):
    def __init__(self, name, age, native_state, native_langauge, location = "India"):
        super().__init__(name, age, location)
        self.native_state = native_state
        self.native_language = native_langauge
```

### Abstraction

What is an abstract class?

An Abstract Class is a superclass that you cannot instantiate.

An Abstract Class has Abstract methods.

NOTE: In Python, an Abstract class must have an abstract method.

These abstract methods are defined in sub-classes that inherits the superclass individually.

2 things to remember about abstract methods:
1. No body in abstract methods. (pass)
2. Sub-classes *must* define the abstract method body.

``` See human_abstract.py ```

### Encapsulation

Encapsulation is the process of keeping attributes and its methods together.

The process of protecting attributes and using methods to get and set (getters and setters) values.

### Polymorphism

Ability of one method to have different implementations in different classes.

### Static methods and Variables

They belong to the class that they are defined in. 
Static methods cannot deal with instance (non-static) methods or attributes.

---

## Projects

### Project 1 - File Organization Automation

