"""
The main benefit of polymorphism is code reusability and flexibility.
It allows you to write generic code that can operate on objects of different classes as long as they share a common interface or base class.
This reduces code duplication and promotes a more modular and maintainable codebase.
"""

class Animal:
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Dog eats dog food!")

class Cat(Animal):
    def eat(self):
        print("Cat eats cat food!")


dog = Dog()
cat = Cat()

# Polymorphism example
def feed(animal):
    # E ca si cum ai creea un buton de feed(care hraneste animale), in loc sa tragi fiecare animal la bolul sau cu mancare.
    animal.eat()

feed(dog)  # Output: Dog eats dog food!
feed(cat)  # Output: Cat eats cat food!

'''
Explicație:

- Numele parametrului din definiția funcției feed() nu influențează modul în care funcția își execută logica.
- Este important ca obiectul transmis ca argument să fie de tipul Animal sau o clasă derivată din Animal.
- Numele variabilei folosite în apelul funcției poate fi diferit de numele parametrului din definiția funcției.
- Ceea ce contează este tipul obiectului transmis și comportamentul metodei eat() care este apelată pe acel obiect.
- Astfel, funcția feed() poate fi apelată cu orice obiect care respectă cerința de a fi de tipul Animal sau o clasă derivată din Animal.
'''