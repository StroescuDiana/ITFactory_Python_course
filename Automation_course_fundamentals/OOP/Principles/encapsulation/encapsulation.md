## Encapsulation
Binding data and functions that manipulate that data within a single unit called class. This hides the internal implementation details and only exposes the public interface.

### Attributes Encapsulation

In Python, `encapsulation` of `attributes` is achieved by:

1. `Public` attributes:

- Have no prefix: `attribute`
- Can be accessed from anywhere
- They can be modified by any code outside the class
- They provide no encapsulation

Definition:
```python
class Car:
    def __init__(self):
        self.color = "White" # public
```

2. `Protected` attributes:

- Start with single underscore: `_attribute`
- Meant to be used within the `class` or its `subclasses`
- They provide a level of encapsulation

Definition:
```python
class Car:
    def __init__(self):   
        self._wheels = 4  # protected
```

3. `Private` attributes:

- Start with double underscores: `__attribute`
- Can only be accessed from `inside` the `class`
- They cannot be accessed directly from outside the class
- To access `private` attributes, you use `getter` and `setter` methods.
- They provide encapsulation

Definition:
```python
class Car:
    def __init__(self):
        self.__model = "Honda" # private
```
Example:

To access `private` attributes, you use `getter` and `setter` methods:
```python
class Car:
  
    def __init__(self):
        self.__model = "Honda"
        
    def get_model(self):
        return self.__model   # getter method
        
    def set_model(self, model):
        self.__model = model # setter method
```

So in summary:

- `Public` attributes - No encapsulation
- `Private` attributes (with `__`) - Maximum encapsulation, accessed via `getters`/`setters`
- `Protected` attributes (with `_`) - Medium encapsulation, accessed within `class` and `subclasses`

Real life example:

Think of a car. The inner workings of the engine, transmission etc. are encapsulated. You only interact with the public interface like steering wheel, pedals, doors etc. Changing the engine does not affect how you drive the car.

```python
class Car:
    
    def __init__(self): 
        self.__model = "Honda" #private attribute
        self.speed = 0
        
    def accelerate(self):
        self.speed += 10
        
    def brake(self):
        self.speed -= 5
        
    def get_model(self):
        return self.__model

car = Car()
car.accelerate()
car.accelerate()
print(car.speed) # 20

# Trying to access private attribute        
#print(car.__model) # AttributeError

# Accessing through public method
print(car.get_model()) # Honda
```
We make the `model` attribute `private` by prefixing it with `double underscores`: `__`.

We provide `public` interface `methods` like `accelerate()`, `brake()` and `get_model()` to interact with the car.

The inner workings like the model are hidden from outside.

We can `change` the engine or transmission without affecting how we drive the car by calling `accelerate()`, `brake()`, etc.

The `public interface` provides `abstraction` by hiding the implementation details of the `private` attributes.


An example Python program demonstrating all types of attribute encapsulation:

```python
class Person:
    
    # Public attributes 
    name = ""   
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Private attribute
    __id = 0
        
    # Protected attribute    
    _gender = ""
    
    # Getter for private attribute    
    def get_id(self):
        return self.__id  
        
    # Setter for private attribute    
    def set_id(self, id):
        self.__id = id
        
    # Methods can access protected attributes      
    def set_gender(self, gender):
        self._gender = gender
        
# Public attribute can be accessed directly        
person = Person("John", 30)       
print(person.name)

# Private attribute accessed via getter
print(person.get_id())

# Private attribute set via setter 
person.set_id(101)      

# Protected attribute accessed within class        
person.set_gender("Male")       
print(person._gender) 

# Inherited class     
class Employee(Person):
      
    # Can access protected attribute of parent class (Person class in this case)   
    def print_gender(self):
        print(self._gender)         

emp = Employee("Jane", 25) 
emp.set_gender("Female")
emp.print_gender()
```
Output:
```commandline
John
0
Male   
Female
```

This demonstrates:

- `Public` attributes accessed directly
- `Private` attributes accessed via getters/setters
- `Protected` attributes accessed within class and subclasses

Here's another example of encapsulation in Python:

```python
class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private attribute
        self.__balance = balance                 # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

# Create a BankAccount object
account = BankAccount("123456789", 1000)

# Get the current balance
balance = account.get_balance()
print("Initial balance:", balance)  # Output: 1000

# Deposit money into the account
account.deposit(500)
balance = account.get_balance()
print("Balance after deposit:", balance)  # Output: 1500

# Withdraw money from the account
account.withdraw(800)
balance = account.get_balance()
print("Balance after withdrawal:", balance)  # Output: 700

# Trying to withdraw more than the balance
account.withdraw(1000)
balance = account.get_balance()
print("Balance after second withdrawal:", balance)  # Output: Insufficient balance.

# Accessing private attributes directly (not recommended)
# print(account.__account_number)  # Raises an AttributeError
# print(account.__balance)  # Raises an AttributeError

# Accessing private attributes using name mangling
print(account._BankAccount__account_number)  # Output: 123456789
print(account._BankAccount__balance)  # Output: 700
```

In this example, we define a `BankAccount` class with two private attributes (`__account_number` and `__balance`) and three public methods (`deposit`, `withdraw`, and `get_balance`). The private attributes are not visible from outside the class, but the public methods provide a controlled interface to access and modify the object's state.

The `deposit` method allows you to deposit money into the account by adding the specified amount to the balance. The `withdraw` method allows you to withdraw money from the account by subtracting the specified amount from the balance, but only if the balance is sufficient. The `get_balance` method allows you to retrieve the current balance of the account.

By encapsulating the `account_number` and `balance` attributes and providing controlled access through public methods, we ensure that the object's state is not modified in unauthorized ways and that the object is used correctly.

### Methods Encapsulation:
In OOP, encapsulation is achieved through the use of access modifiers, such as `public`, `private`, and `protected`. 

- `Public` methods and properties are accessible from anywhere, including outside the class.
- `Private` methods and properties are only accessible within the class and are not visible from outside the class.
- `Protected` methods and properties are only accessible within the class and its subclasses.

By encapsulating the internal details of an object and exposing only the necessary interface, you can prevent unauthorized modification of the object's state and ensure that the object is used correctly. Encapsulation also allows you to change the implementation details of the object without affecting the code that uses the object.

#### Private methods/properties
In Python, there is no true concept of private methods or properties, but there is a convention to denote a property or method as private. A private method or property is one that is intended to be used only within the class and not by the code outside of the class.

In Python, you can denote a property or method as private by adding a double underscore prefix before the property or method name. This is known as name mangling. Python will automatically prepend the name of the class to the property or method name to avoid name clashes with properties or methods in subclasses. 

For example, consider the following class:

```python
class MyClass:

    def __init__(self):
        self.__private_property = 42

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()
        print(f"The private property value is {self.__private_property}.")

obj = MyClass()
obj.public_method()

# However, despite the use of name mangling to make the property and method private, 
# it is still possible to access them from outside the class by using the mangled name. 
# For example, you can access the private property and method of the `MyClass` object as follows:
        
obj = MyClass()
print(obj._MyClass__private_property)   # Output: 42
obj._MyClass__private_method()          # Output: "This is a private method."


# obj.__private_property  # Raises an AttributeError

# Calling the private method directly (not recommended)
# obj.__private_method()  # Raises an AttributeError
```

```commandline
Output:
This is a public method.
This is a private method.
The private property value is 42.
```

In this example, the `__private_property` and `__private_method` are denoted as `private` using the double underscore prefix. The `public_method` is a public method that can be accessed from outside the class.

Note that accessing private properties or methods of a class from outside the class is generally discouraged because it can break encapsulation and lead to code that is difficult to maintain. Instead, it is better to rely on the public interface of the class to interact with its properties and methods.


#### Protected methods/properties

In Python, protected methods and properties are denoted with a single underscore prefix before the method or property name. The use of a single underscore prefix is a convention to indicate that a method or property is intended for internal use within the class and its subclasses.

Protected methods and properties can be accessed from within the class and its subclasses but not from outside the class.

Here's an example of a class with a protected property and method:

```python
class MyClass:
    def __init__(self):
        self._protected_property = 42

    def _protected_method(self):
        print("This is a protected method.")

    def public_method(self):
        print("This is a public method.")
        self._protected_method()
        print(f"The protected property value is {self._protected_property}.")
```

In this example, the `_protected_property` and `_protected_method` are denoted as protected using the single underscore prefix. The `public_method` is a public method that can be accessed from outside the class.

However, it is generally recommended to avoid accessing protected methods or properties from outside the class or its subclasses. Instead, you should rely on the public interface of the class to interact with its properties and methods.

It's worth noting that the use of single or double underscores to denote private or protected members in Python is just a convention. In Python, there is no true concept of private or protected members, and it is still possible to access them from outside the class if you know their names. The convention is intended to discourage direct access to these members and encourage the use of the public interface of the class instead.

#### Public methods/properties

In Python, public methods and properties are those that do not have any prefix before their name. They are accessible from within the class, its subclasses, and from outside the class.

Here's an example of a class with a public property and method:

```python
class MyClass:
    def __init__(self):
        self.public_property = 42

    def public_method(self):
        print("This is a public method.")
        print(f"The public property value is {self.public_property}.")
```

In this example, the `public_property` and `public_method` are denoted as public without any prefix. The `public_method` can be accessed from outside the class as well.

Public methods and properties are the primary way to interact with an object from outside the class. They are the interface to the object and allow you to get or set the object's state, call its behavior, and interact with its data.

It's important to note that while public methods and properties are accessible from outside the class, it is still important to design them carefully. You should ensure that they provide a safe and consistent interface for interacting with the object and that they do not expose any implementation details that could break encapsulation.


Complete code sample using all types of encapsulation for both methods and attributes:
```python
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute
        self.__secret = "I have a secret"  # Private attribute

    def say_name(self):
        print(self._name)

    def __greeting(self):
        print(f"Hello, I am {self._name}")

    def set_name(self, name):
        self._name = name
        self.__greeting()

    def _calc_age(self, years):
        self._age += years

    def say_age(self):
        print(self._age)

# Create a Person object
person = Person("John", 30)

# Call public method
person.say_name()  # Output: John
person.say_age()  # Output: 30

# Access protected attribute
print(person._name)  # Output: John

# Modify protected attribute
person._name = "Jane"
person.say_name()  # Output: Jane

# Call setter method (calls private method)
person.set_name("Alice")  # Output: Hello, I am Alice

# Access private attribute (will raise an AttributeError)
# print(person.__secret)
```

