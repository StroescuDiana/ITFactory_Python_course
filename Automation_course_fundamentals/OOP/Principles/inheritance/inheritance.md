## Inheritance
The ability to create new classes from existing classes inheriting their properties and behaviors. This allows for code reusability.

Real life example:

For example, a Dog is a Mammal. So the Dog class can `inherit` from the Mammal class and `reuse` properties like heartbeat, birth process etc.
```python
class Animal:
    alive = True
    
class Mammal(Animal):
    heartbeat = True
    
class Dog(Mammal):    
    breed = "Labrador"
```
Here Dog `inherits` from Mammal which itself `inherits` from Animal. Dog reuses alive and heartbeat but also has its own breed property.

**Inheritance** is a fundamental feature of object-oriented programming that allows a new class to be based on an existing class. The new class **inherits the properties and methods of existing class**, and can also **add new properties and methods of its own**.

The existing class is called the **superclass** or **parent class**, and the new class is called the **subclass** or **child class**.
```python
# Define a superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hi!")


# Define a subclass that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks!")

# Create an instance of the superclass
animal = Animal("Generic animal")
animal.speak()

# Create an instance of the subclass
dog = Dog("Fido", "Golden Retriever")
dog.speak()
print(dog.breed)
```

In this example, we define a superclass `Animal` with a constructor and a `speak` method.
We then define a subclass `Dog` that inherits form `Animal` and adds a new `breed` attribute and overrides the `speak` method. We create an instance of the superclass and call its `speak` method, and then create an instance of the subclass and call its `speak` method and print its `breed` attribute.

Output:
```commandline
Generic animal says hi!
Fido barks!
Golden Retriever
```

As you cand see, the `Dog` subclass inherits the `__init__` and `speak` methods from the `Animal` superclass, and we can also add new attributes and override the existing ones in the subclass.


Automation Testing Inheritance:
```python
class Automation:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name} test")


class LoginAutomation(Automation):
    def __init__(self, name, username, password):
        super().__init__(name)
        self.username = username
        self.password = password

    def run(self):
        super().run()
        print(f"Logging in with username: {self.username} and password: {self.password}")


class SearchAutomation(Automation):
    def __init__(self, name, keyword):
        super().__init__(name)
        self.keyword = keyword

    def run(self):
        super().run()
        print(f"Performing search for keyword: {self.keyword}")


# Create instances of the classes
login = LoginAutomation("Login Automation", "john_doe", "secretpassword")
search = SearchAutomation("Search Automation", "Python tutorials")

# Call the run method
login.run()
search.run()
```

In this example, we have a base class `Automation` that represents a generic automation task. It has an `__init__()` method to initialize the `name` of the automation and a `run()` method to execute the automation.

Two derived classes, `LoginAutomation` and `SearchAutomation`, `inherit` from the `Automation` class. Each of these classes extends the functionality by adding additional attributes and `overriding` the `run()` method to include specific actions.

The `LoginAutomation` class represents an automation task for logging in, taking additional parameters for the username and password. The `SearchAutomation` class represents an automation task for performing a search, taking a keyword parameter.

We create `instances` of the derived classes (login and search) and call the `run()` method on each instance. The `run()` method of the respective class is executed, and the appropriate actions are performed based on the specific automation task.