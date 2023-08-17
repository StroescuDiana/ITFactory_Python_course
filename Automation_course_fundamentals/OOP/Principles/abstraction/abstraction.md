## Abstraction
Hiding unnecessary details and only exposing relevant details. This makes the code more readable and maintainable.

1. `Defining` abstract base classes using `ABC` (Abstract Base Classes) module:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    pass
```
This `defines` an `abstract base class` Vehicle. It cannot be instantiated, and serves as a blueprint for subclasses.

2. `Adding` abstract methods using `@abstractmethod` decorator:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
```
Abstract methods are placeholder methods that must be implemented by concrete subclasses.

3. `Implementing` subclass/es that `inherit` from the abstract base class:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("Car is going!")
```
The Car class `inherits` from Vehicle and `implements` the `go()` abstract method.

4. Only concrete subclasses can be `instantiated`:
    

    car = Car()

5. Abstract base classes define an interface that is shared by concrete subclasses:


    vehicle = Car()  
    vehicle.go()     
    
    vehicle = Bike()           
    vehicle.go()


Here we use the `abstract` Vehicle interface to call the `go()` method, hiding the concrete Car or Bike implementation.


Real life example:

The Vehicle `abstract` class defines the relevant interface `go()` and `stop()` without implementing it. Subclasses implement these abstract methods based on their specifics. We `hide` the implementation details and expose only the public interface.
```python
from abc import ABC, abstractmethod  

class Vehicle(ABC):    
   
    # Abstract methods      
    @abstractmethod    
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):      
        pass
    
# Concrete class      
class Car(Vehicle):
    
    def go(self):
        print("Car is going...")
        
    def stop(self):
        print("Car is stopping.")
        
# Another concrete class
class Bike(Vehicle):
    
    def go(self):
        print("Bike is moving...")
        
    def stop(self):
        print("Bike is stopping...")
        
# Create objects   
car = Car()
car.go()
car.stop()

bike = Bike()     
bike.go()     
bike.stop()
```

This demonstrates abstraction through:

The `abstract` Vehicle class:

- Defines the interface with `abstract` methods `go()` and `stop()`
- Does **NOT** implement the functionality

- The concrete `Car` and `Bike` classes:
  - Implement the abstract methods based on their specifics

- The interface (`abstract` Vehicle class) is separated from the implementation (`concrete` subclasses)

- The user of the API only interacts with the abstract Vehicle interface, hiding the concrete implementations.

This provides:

**Modularity**: Concrete classes can be modified without affecting the interface

**Reusability**: The interface can be reused by multiple subclasses

**Information hiding**: Implementation details are abstracted away

Abstraction helps us simplify complex systems by focusing on the relevant aspects and providing a clear interface for interacting with them, promoting code reusability and maintainability.

**So in summary:**

- Abstract base classes define an interface (abstract methods)
- Concrete subclasses implement that interface
- The interface is separated from implementation
- Only concrete classes can be instantiated
- The abstract class exposes a shared interface that hides implementations.


**This provides benefits like:**

- Information hiding
- Reusability
- Flexibility
- Maintainability

Here's another example of an abstract class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

In this example, the `Shape` class is an abstract class that defines two **abstract methods** `area()` and `perimeter()`. These methods **must** be implemented by any subclass of `Shape`, but the implementation details are left to the subclasses themselves. This allows us to define a common interface for all shapes, but the details of how each shape calculates its area and perimeter are left to the specific shape classes.

Interfaces, on the other hand, are similar to abstract classes but contain only abstract methods. They are used to define a common interface that all classes implementing the interface must adhere to. In Python, there is no separate keyword for interfaces, but you can achieve the same effect by defining an abstract base class that contains only abstract methods.

Abstraction allows you to design more flexible and extensible code by separating the interface from the implementation details. This makes it easier to change the implementation details without affecting the code that uses the interface, and it also makes it easier to extend the code with new functionality by creating new subclasses or implementing new interfaces.
