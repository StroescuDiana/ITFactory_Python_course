# Polymorphism

`Polymorphism` is the ability of objects to take on `different forms` depending on the context in which they are used. In Python, polymorphism is achieved through the use of method `overloading`, method `overriding`, and `duck typing`.

First example of taking different forms using inheritance:

```python
class Vehicle:
    def go(self):
        print("Going...")

class Car(Vehicle):
    def go(self):
        print("Driving fast!")

class Motorcycle(Vehicle): 
    def go(self):
        print("Zoooom!")

# We can use the parent class interface     
car = Car()       
motorcycle = Motorcycle()

car.go() # Driving fast!
motorcycle.go() # Zoooom!
```
Here we have a `Vehicle` parent class defining the `go()` method. The Car and `Motorcycle` classes `inherit` from `Vehicle` and implement the `go()` method in their own way.

Another example:<br>
A parent class may have a method `eat()`. Subclasses can define their own version of `eat()` based on what they eat.

```python
class Animal:
    def eat(self):
        pass
    
class Dog(Animal):
    def eat(self):
        print("Dog eats dog food!")
        
class Cat(Animal):        
    def eat(self):
        print("Cat eats cat food!")


animal = Animal()
animal.eat()  # No specific eat() implementation in Animal class

dog = Dog()
dog.eat()  # Output: Dog eats dog food!

cat = Cat()
cat.eat()  # Output: Cat eats cat food!

# Polymorphism example
def feed(animal):
    animal.eat()

feed(dog)  # Output: Dog eats dog food!
feed(cat)  # Output: Cat eats cat food!
```
Here the `eat()` method has `different forms` based on the subclass, but we call it using the parent interface Animal.

**Duck Typing:**

Duck typing is a concept in Python that focuses on an object's behavior rather than its type. 
It allows different objects to be used interchangeably if they implement the same methods or have the same attributes, regardless of their specific class or inheritance hierarchy. 

In Python, `duck typing` polymorphism means that if an object walks like a duck and quacks like a duck, then it can be treated as a duck. In other words, if an object supports the necessary methods or attributes required by a particular operation, it can be used in that context, even if it doesn't explicitly inherit from a specific class or implement a particular interface.

```python
class Duck:
    def quack(self):
        print("Quack!")

    def walk(self):
        print("Walking like a duck.")

class Dog:
    def bark(self):
        print("Woof!")

    def walk(self):
        print("Walking like a dog.")


def make_animal_walk(animal):
    animal.walk()


# Create objects
duck = Duck()
dog = Dog()

# Call the function with different objects
make_animal_walk(duck)  # Duck walks like a duck
make_animal_walk(dog)   # Dog walks like a dog
```
In this example, we have a `Duck` class and a `Dog` class, both of which have a `walk` method. We also have a function `make_animal_walk` that takes an animal argument and calls its walk method.

Even though the `Duck` and `Dog` classes are unrelated and don't share a common base class or interface, we can still pass objects of these classes to the `make_animal_walk` function. This is because both objects have a `walk` method, which is the only requirement for the function.

**Method overloading**

Python does **NOT** support method `overloading`. Method `overloading` allows a class to have multiple methods with the same name but different `signatures` (different numbers or types of arguments).

Python does not support method `overloading` in the traditional sense, but you can achieve similar behavior by using default arguments or variable-length argument lists.

So how do we emulate method overloading in Python?

There are a few approaches:
1. Variable Number of Arguments: `*args`, `**kwargs`:
- You can accept a variable number of arguments, and check the types inside the method:

```python
def sum_overload(*args):
    total = 0

    # Check if all args are int
    all_int = True
    for arg in args:
        if not isinstance(arg, int):
            all_int = False
            break

    if all_int:
        # Sum all int arguments
        for arg in args:
            total += arg

    else:
        # Convert all args to float and sum
        for arg in args:
            total += float(arg)

    return total


# Call with ints
result = sum_overload(1, 2)
print(result)  # 3

# Call with floats
result = sum_overload(1.7, 2.5)
print(result)  # 4.2
```

2. Pass the Type as an Argument:
- You can pass the type as an argument and call different implementations:

```python
def sum(a, b, typ):
    if typ == "int":
       return int_sum(a, b)
    elif typ == "float":
       return float_sum(a, b)

def int_sum(a, b):    
    return a + b

def float_sum(a, b):   
    return a + b  

print(sum(1, 2, "int")) # 3
print(sum(1.5, 2.5, "float")) # 4.0
```

**Method overriding**

Method `overriding` in Python refers to the ability to `redefine` a method in a `child` class that is already defined in the `parent` class.
Polymorphism in this case is achieved using `inheritance`. A parent class defines an interface, with child classes implementing that interface in different ways.

```python
class Parent:
    def say_hello(self):
        print("Hello from Parent!")
        
class Child(Parent):
    def say_hello(self):
        print("Hello from Child!")
        
parent = Parent()
parent.say_hello() # Hello from Parent!

child = Child()  
child.say_hello() # Hello from Child!


parent = Parent()
child = Child()

print(parent.say_hello()) # Parent hello
print(child.say_hello()) # Child hello
```
Here we have:

- A `Parent` class with a `say_hello()` method
- A `Child` class that `inherits` from Parent
- The `Child` class `redefines` the `say_hello()` method
- 
When we call the method on the Parent class, it prints the Parent message.  But when we call it on the Child class, it prints the Child message, `overriding` the Parent's `method`.

This allows the `Child` class to `redefine` or `override` the behavior of a `method` defined in the `Parent` class.

Example of Polymorphism used in combination with Abstraction:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

shapes = [Circle(5), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```

In this example, we define two `concrete` classes Circle and Rectangle that `inherit` from the `abstract` class Shape. Each class provides its own implementation of the `area` and `perimeter` methods based on its specific shape.

We then create a list of shapes that contains an instance of Circle and an instance of Rectangle. We can then iterate over the list and call the `area()` and `perimeter()` methods on each shape, without needing to know the specific class of each shape. This demonstrates the idea of `duck typing` and dynamic polymorphism, where objects that have the same interface can be used interchangeably, regardless of their actual class or type.

Example of Polymorphism:

```python
# Method overloading
class Math:
    
    @classmethod
    def sum(cls, a, b, typ="int"):
        if typ == "int":
            return cls.int_sum(a, b)
        if typ == "float": 
            return cls.float_sum(a, b)
            
    @classmethod       
    def int_sum(cls, a,b):
        return int(a) + int(b)
                
    @classmethod      
    def float_sum(cls, a, b):
        return float(a) + float(b)

# Method overriding        
class ChildMath(Math):
    
    @classmethod
    def int_sum(cls, a, b):
        return int(a) * int(b)


# Call parent sum
result = Math.sum(1, 2)
print(result)  # Output: 3

# Call child sum
result = ChildMath.sum(1, 2)
print(result)  # Output: 2

# Call float sum in child
result = ChildMath.sum(1.7, 2.5, "float")
print(result)  # Output: 4.2

# Call parent sum with float numbers
result = Math.sum(1.8, 2.5, "float")
print(result)  # Output: 4.3

# Call parent sum with different types
result = Math.sum("10", 5.5, "float")
print(result)  # Output: 15.5

# Call child sum with different types
result = ChildMath.sum("10", 5.5, "float")
print(result)  # Output: 10.0
```