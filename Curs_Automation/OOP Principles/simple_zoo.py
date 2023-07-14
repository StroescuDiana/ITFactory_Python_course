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