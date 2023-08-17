# Object-Oriented Programming Principles:

Here’s a brief overview of the `4` main `principles` of OOP:

`Abstraction` refers to the practice of showing only the necessary details and hiding the complexity. This can be achieved through the use of interfaces and abstract classes.

`Encapsulation` is the practice of keeping an object’s state private and providing public methods to interact with that state. This helps to maintain the integrity of the object’s data.

`Inheritance` allows new objects to take on the properties and methods of existing objects. This can help to reduce code duplication and improve code organization.

`Polymorphism` allows objects to be treated as a member of their own class, or as a member of a parent class. This can make it easier to write more flexible and reusable code.


ZOO simulation applying all OOP Principles:
```python
class Animal:
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age

    def __str__(self):
        return f"{self._name} is a {self._age} year old {self._species}"

    def speak(self):
        raise NotImplementedError("Subclass must implement speak method")

class Mammal(Animal):
    def __init__(self, name, species, age, is_domesticated):
        super().__init__(name, species, age)
        self._is_domesticated = is_domesticated

    def is_domesticated(self):
        return self._is_domesticated

class Reptile(Animal):
    def __init__(self, name, species, age, is_venomous):
        super().__init__(name, species, age)
        self._is_venomous = is_venomous

    def is_venomous(self):
        return self._is_venomous

class Dog(Mammal):
    def __init__(self, name, age, breed, is_domesticated=True):
        super().__init__(name, "Dog", age, is_domesticated)
        self._breed = breed

    def speak(self):
        return "Woof!"

class Cat(Mammal):
    def __init__(self, name, age, breed, is_domesticated=True):
        super().__init__(name, "Cat", age, is_domesticated)
        self._breed = breed

    def speak(self):
        return "Meow!"

class Snake(Reptile):
    def __init__(self, name, age, species, is_venomous):
        super().__init__(name, species, age, is_venomous)

    def speak(self):
        return "Sssss!"

if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "Maine Coon")
    snake = Snake("Nagini", 5, "Python", False)

    animals = [dog, cat, snake]

    for animal in animals:
        print(animal) # Polymorphism: __str__()
        print(animal.speak()) # Polymorphism: speak()
```

```commandline
Output:
Buddy is a 3 year old Dog
Woof!
Whiskers is a 2 year old Cat
Meow!
Nagini is a 5 year old Python
Sssss!
```

Here's a brief explanation of how the OOP principles are used in the code:

**Encapsulation**: `Animal`, `Mammal`, and `Reptile` classes have `private` attributes (e.g. _name, _species, _age), and the subclasses have their own private attributes (e.g. _is_domesticated, _is_venomous, _breed).

**Inheritance**: `Mammal` and `Reptile` classes `inherit` from `Animal`, and `Dog`, `Cat`, and `Snake` classes `inherit` from `Mammal` and `Reptile`.

**Polymorphism**: The `speak()` method is implemented differently in each of the `Dog`, `Cat`, and `Snake` classes, allowing them to be called in a loop on a list of mixed animal objects.

**Abstraction**: The `speak()` method in the `Animal` class is an `abstract` method that **must** be implemented in subclasses, ensuring that any class that `inherits` from `Animal` must provide an implementation for it.
