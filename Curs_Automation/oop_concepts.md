# OOP Concepts

## Class

### What is a class?
A `class` is a blueprint or a template for creating `objects`. It defines a set of `attributes` and `methods` that an object of that class can have.

    class Car:
        pass

### What is an object?

An `object` is an instance of a class. Objects have:

- **State**: represented by `attributes`/properties of the object. The values of these attributes define the state of the object.

- **Behavior**: represented by `methods` of the `object`. Methods implement the functionality of the object.


    my_car = Car()


### What are attributes? 

`Attributes` are properties or characteristics that describe an `object`. They define the object's `state`.

For example, in a Dog class:

- name is an attribute - it stores the name of the dog
- age is an attribute - it stores the age of the dog
- color is an attribute - it stores the color of the dog's fur


    class Dog:
    name = ""  
    age = 0    
    color = ""

### What are methods?

`Methods` are functions defined inside a class. They encapsulate the `behavior` of an `object`.

For example, in a Dog class we could have:

- a `bark()` method that prints "Woof!"
- an `eat()` method that prints "Munch munch!"
- these methods define what the dog can do. They represent the dog's behavior.


    class Dog:
    
    def bark(self):
        print("Woof!")
        
    def eat(self):
        print("Munch munch!")


```python
class Dog:
    """A simple Dog class"""
    
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("Woof!")

# Creating an object from the Dog class      
rover = Dog("Rover")

# Accessing an attribute of the object        
print(rover.name)  # Prints Rover

# Calling a method on the object        
rover.bark()  # Prints Woof!
```
Here:

- Dog is a `class` that defines the blueprint for Dog objects.

- rover is an `object` instantiated from the Dog class.

The object rover has:

- `State`: represented by the name `attribute` with value "Rover"
- `Behavior`: represented by the bark() `method`.

The difference between `methods` and `functions` is:

- Methods are defined within a `class`, functions are defined at the module level.
- Methods have an implicit first argument named `self` that refers to the instance of the class. Functions do not have this.
- Methods operate on an `object` and its `attributes`, functions operate on passed arguments.
- Methods are bound to a class and object, functions belong to a module.


### Class variables 

There are three different types of class variables: `instance` variables, `class` variables, and `static` variables. 

**1. Instance Variables:**

Instance variables are unique to each instance (object) of a class. They are defined within methods using the `self` keyword and are accessed using the `self` prefix.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.brand)  # Output: Toyota

```

In this example, `brand` and `model` are instance variables specific to each Car object. Every time a new `Car` object is created, it will have its own separate brand and model attributes.

**2. Class Variables:**

Class variables are shared among all `instances` of a class. They are defined within the class but outside any methods. Class variables are accessed using the class name or an instance.

```python
class Car:
    wheels = 4

my_car = Car()
print(my_car.wheels)  # Output: 4

other_car = Car()
print(other_car.wheels)  # Output: 4

Car.wheels = 6
print(my_car.wheels)  # Output: 6
print(other_car.wheels)  # Output: 6
```

In this example, `wheels` is a class variable that is shared among all `Car` objects. Any changes made to `wheels` will be reflected in all instances. Class variables are accessed using the class name or an instance of the class.

**3. Static Variables:**

Static variables are similar to class variables but have a slightly different usage. They are defined within the class, but they are not accessed or modified by instances or instance methods. They are typically used for storing constants or utility variables.

```python
class MathUtils:
    PI = 3.14159

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.PI)  # Output: 3.14159
print(MathUtils.multiply(5, 2))  # Output: 10

```
In this example, `PI` is a `static` variable that stores the value of pi. The `multiply()` method is a `static` method that does not have access to instance variables but can access static variables.

Static variables are accessed using the class name, just like class variables, and they can also be accessed within static methods.


**Static variables and methods in Python are used to define variables and methods that are shared among all instances of a class:**

```python
class Dog:
    
    count = 0 # static variable 
    
    def __init__(self):
        Dog.count += 1
        
    @staticmethod    
    def num_dogs(): # static method
        print("Number of dogs:", Dog.count)

rover = Dog()
print(Dog.count) # 1

fido = Dog()
print(Dog.count) # 2

Dog.num_dogs() # Number of dogs: 2
```
Here:

- count is a `static variable`. It is shared among all Dog objects and initialized only once. 
- num_dogs() is a `static` method`. It can be called without an instance of the Dog class.


### Example for what We've learned so far:
```python
class Human:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
john = Human("John","Doe",30)
```

```python
class Human:
    
    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
     
    def describe(self):
        # describe is a local variable, only present in describe() method
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)    
        
    @classmethod
    def getTribe(cls):
        return cls.tribe
        # In this case, getTribe() is a class method that accesses the tribe attribute on the class, not the instance. 
        # This means it will return the tribe for the entire Human class, not for an individual human instance.
    
    @staticmethod
    def human_wikipedia_definition():
        print("Humans (Homo sapiens) are the most common and widespread species of primate in the great ape family Hominidae.")


# Example 1 of OOP

# Create a Human object
person = Human("John", "Doe", 30)

# Access instance variables
print(person.first_name)  # Output: John
print(person.last_name)  # Output: Doe
print(person.age)  # Output: 30

# Access class variable
print(Human.tribe)  # Output: Hominina

# Call the describe method
person.describe()  # Output: My name is John Doe and I am 30 years old.


# Example 2 of OOP
print(Human.getTribe())


# Example 3 of OOP
john = Human("John","Doe",30)
john.human_wikipedia_definition()

Human.human_wikipedia_definition()
```

```python
class Person:
    
    population = 0
        
    def __init__(self, name):
        self.name = name
        Person.population += 1
        
        # Initiate collections
        self.interests = []  
        self.friends = []
        
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
    def display_info(self):
        print(f"Name: {self.name} Interests: {self.interests} Friends: {self.friends}")
        
    def add_interest(self, interest):
        self.interests.append(interest)
        
    def add_friend(self, friend):
        self.friends.append(friend)
        
    @classmethod
    def get_population(cls):
        return cls.population

john = Person("John")  
john.add_interest("Music")
john.add_friend("Jack")

jack = Person("Jack")

print(Person.get_population()) # 2
```
**Class Model:**

So this Person class models the basic properties and functionality of a person, like:

- Name
- Interests
- Friends
- Greeting others
- Displaying information

This class has:

- A `static variable` population which keeps track of the total number of Person objects created.
- `Attributes` like name, interests, and friends.
- A `constructor` that initializes the `attributes` and increments the population.
- `Methods` like greet() to introduce themselves, display_info() to show all info, and `methods` to add interests and friends.
- A class `method` get_population() to return the total population.


```python
class Animal:
    # Class variable
    species = "Unknown"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        self.health = 100  # instance variable

    # Instance method
    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    # Class method
    @classmethod
    def get_species(cls):
        return cls.species

    # Static method
    @staticmethod
    def sleep():
        print("The animal is sleeping.")

    # Setter method
    def set_health(self, health):
        self.health = health

    # Getter method
    def get_health(self):
        return self.health


# Creating instances of the Animal class
lion = Animal("Simba", 5)
tiger = Animal("Rajah", 3)

# Accessing instance variables
print(lion.name)  # Output: Simba
print(lion.age)  # Output: 5

# Accessing class variable
print(Animal.species)  # Output: Unknown

# Accessing instance methods
lion.eat("meat")  # Output: Simba is eating meat.
tiger.sleep()  # Output: The animal is sleeping.

# Using setter and getter methods
lion.set_health(90)
print(lion.get_health())  # Output: 90
```

In this example, the Animal class demonstrates the following:

- Class variable (species): It is a variable shared by all instances of the class and accessed using the class name (Animal.species).

- Instance variables (name, age, health): These variables store unique values for each instance of the class (lion, tiger).

- Instance method (eat()): It is a method that operates on an instance of the class and takes a parameter (food).

- Class method (get_species()): It is a method that operates on the class itself and does not require an instance. It uses the class name (Animal.species).

- Static method (sleep()): It is a method that operates on the class itself and does not require an instance. It does not use any instance or class variables.

- Setter and getter methods (set_health(), get_health()): These methods provide access to a private instance variable (health) and allow setting and retrieving its value.


```python

```

