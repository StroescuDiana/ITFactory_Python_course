# Functions, Parameters, Functions with undefined parameters number, Exceptions, Debugging

## Functions 
Functions in Python are blocks of reusable code that perform a specific task. They allow you to divide your code into logical and modular pieces, making it easier to understand, debug, and maintain. Functions take input arguments (parameters), perform a series of operations, and return a result.

**Function Definition:** 

Start by defining a function using the def keyword, followed by the function name and parentheses. You can also specify parameters inside the parentheses if the function requires input values.

```python
# Function definition block
def greet():
    print("Hello, world!")

# Function call 
# To execute the code inside a function, you need to call it by its name, followed by parentheses.
greet() 

# Output: Hello, world!
```

**Return Statement:** 

Functions can also return values back to the caller using the `return` statement. You can use this to pass data or results back from the function.

```python
# Function definition
def add(a, b):
    return a + b

result = add(3, 5)
# Function call 
print(result) # Output: 8
```
Functions are an essential concept in programming that allow you to encapsulate a block of code and execute it whenever needed. They play a crucial role in organizing and structuring your code, making it more modular, readable, and reusable.

**Conclusion:**

We decide to implement a function when we know we have instructions that need to be executed multiple times in our program.


## Parameters in Functions

Parameters in functions are placeholders for values that can be passed into the function when it is called. They allow functions to receive input data and operate on it. Parameters represent the inputs or arguments required by a function to perform its task.

When defining a function, you can specify parameters inside the parentheses. These parameters act as variables within the function's scope, holding the values passed when the function is called.

There are two types of parameters in Python: `explicit` parameters and `implicit` parameters.

**Explicit Parameters:** 

These are parameters explicitly defined in the function definition. They are listed inside the parentheses, separated by commas. `Explicit` parameters allow you to define the specific inputs your function expects.

```python
def greet(name):
    print("Hello, ", name)

greet("Alice") # Output: Hello, Alice
```
In this example, name is an `explicit` parameter. When calling the greet function, you need to pass a value for the name parameter.

**Implicit Parameters:** 

These parameters are not explicitly defined in the function definition, but they represent a general category of input values. `Implicit` parameters are typically used within specific contexts or conventions.

For example, in object-oriented programming, the first parameter of a method is usually called `self`. It represents the instance of the class and allows the method to access the object's attributes and methods.

**A example in object-oriented programming:**
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Access attribute using self

    def bark(self):
        print(f"Woof! My name is {self.name}")


shelty = Dog("Shelty")
shelty.bark()  # Woof! My name is Shelty
```
In the above example, `self` is used as an `implicit` parameter within a method definition. The use of `self` is commonly seen in object-oriented programming, specifically when defining methods within a `class`.

- `self` is an `implicit` parameter, not explicitly passed when calling the function
- It provides access to variables within the scope/context the function is called in
- In this example, that scope is the global scope, so self refers to the global variables

**Implicit vs Explicit parameters**

`Implicit` and `Explicit` parameters in Python functions serve different purposes and have distinct characteristics:

**Explicit Parameters:**
- Explicit parameters are defined explicitly in the function definition.
- They are listed inside the parentheses and act as placeholders for values that are passed when calling the function.
- Explicit parameters provide a way to receive input values from the caller and work with them within the function's scope.
- They allow the function to be more flexible and adaptable by accepting different inputs based on specific requirements.

**Implicit Parameters:**
- Implicit parameters are not explicitly defined in the function definition.
- They represent a built-in or predefined aspect of the function or its context.
- Implicit parameters are typically associated with certain conventions, contexts, or object-oriented programming concepts.
- They provide additional functionality or behavior to the function, beyond the explicit parameters.

**Examples that use different kinds of parameters:**

_Example 1:_

```python
# globally declared variables
name = "John"
age = 30

def greet():
    print(f"Hello, my name is {name} and I'm {age} years old.")

greet()
# Hello, my name is John, and I'm 30 years old.
```
Here, the `greet()` function has access to the global `name` and `age` variables as `implicit` parameters.

_Example 2:_

```python
name = "John"

def greet(person_name, person_age):
    print(f"Hello, my name is {person_name} and I'm {person_age} years old.")
    
age = int(input("Enter your age: "))
greet(name, age)  
# Hello, my name is John, and I'm 30 years old.
```
Here, `person_name` and `person_age` are `explicit` parameters that we pass when calling the `greet()` function. We also prompt the user for their age and pass it as an argument.

_Example 3:_

```python
names = ["John", "Jane", "Jim"]

def greet_all():
    for name in names:
        print(f"Hello, my name is {name}")

greet_all()   
# Hello, my name is John         
# Hello, my name is Jane
# Hello, my name is Jim
```
Here, the `greet_all()` function has `implicit` access to the `global` names list, which it then iterates over to greet each name.

_Example 4:_

```python
def greeting(first_name, last_name):
    print(first_name + " " + last_name)

greeting(last_name = "Pop", first_name = "Mihai") # Output: Mihai Pop
```
_Keyword parameters:_ You specify the parameter name when calling the function. The order does not matter.

_Example 5:_

```python
def greeting(fname, lname, greeting="Hello"):
    print(greeting + " " + fname + " " + lname)

greeting("John", "Smith")    # Hello John Smith  
greeting("John", "Smith", "Hi") # Hi John Smith
```
_Default parameters:_ You assign a default value to a parameter in the function definition. If a value is not provided when calling the function, it uses the default.

_Example 6:_

```python
def sum_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_nums()) # 0
print(sum_nums(1, 2, 3)) # 6
print(sum_nums(1, 2, 3, 4, 5)) # 15
```
_Variable length parameters:_ You use `*args` to pass a variable number of arguments to a function. The arguments are received as a `tuple`.

**Conclusion:** _Parameters in Python functions refer to the information you pass into the function, so it can perform a specific task._

## Understanding *args in Python Functions

In Python, `*args` is a special syntax that allows a function to accept a variable number of positional arguments. The `*args` parameter enables you to pass an arbitrary number of arguments to a function without explicitly specifying them in the function definition. It collects all the positional arguments passed and packs them into a `tuple`.

```python
def greet(*args):
    print(args) # ('Alice', 'Bob', 'Charlie')
    for name in args:
        print("Hello,", name)

greet("Alice", "Bob", "Charlie")
```
Output:

    Hello, Alice
    Hello, Bob
    Hello, Charlie

## Automation Testing Example: Using *args for Test Case Parameters

In an automation testing scenario, `*args` can be helpful when you have a variable number of test case parameters. Let's consider an example where we want to write a function to execute test cases for a web application. Each test case might have different parameters, such as URL, input values, expected outputs, etc. The `*args` parameter allows us to handle this flexibility.

```python
def execute_test_case(test_name, *args):
    print("Running test case:", test_name)
    print("Test case parameters:", args)

    if test_name == "Login Test":
        url, username, password = args
        # Simulating login test case
        if username == "user123" and password == "pass456":
            print("Login successful.")
        else:
            print("Login failed.")
    elif test_name == "Registration Test":
        url, username, email = args
        # Simulating registration test case
        if len(username) > 0 and "@" in email:
            print("Registration successful.")
        else:
            print("Registration failed.")
    else:
        print("Unknown test case.")

# Example usage
execute_test_case("Login Test", "https://example.com", "user123", "pass456")
execute_test_case("Registration Test", "https://example.com", "user123", "email@example.com")
```

Output:

    Running test case: Login Test
    Test case parameters: ('https://example.com', 'user123', 'pass456')
    Login successful.
    Running test case: Registration Test
    Test case parameters: ('https://example.com', 'user123', 'email@example.com')
    Registration successful.

The above example but this time introducing the data from keyboard:

```python
def execute_test_case(test_name, *args):
    print("args input: ", args)
    print("Running test case:", test_name)
    print("Test case parameters:", args)

    if test_name == "Login Test":
        url, username, password = args
        # Simulating login test case
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")

        if username == input_username and password == input_password:
            print("Login successful.")
        else:
            print("Login failed.")
    elif test_name == "Registration Test":
        url, username, email = args
        # Simulating registration test case
        print("Registration successful.")

        # Prompt for login credentials
        login_username = input("Enter username: ")
        login_password = input("Enter password: ")

        # Execute login test case
        execute_test_case("Login Test", url, login_username, login_password)
    else:
        print("Unknown test case.")

# Example usage
execute_test_case("Registration Test", "https://example.com", "user123", "email@example.com")
```

## Understanding **kwargs in Python Functions

In python, `**kwargs` is a special syntax that allows a function to accept a variable number of keyword arguments. The term `kwargs` is a convention, but you can choose any valid variable name.

**Defining a Function with **kwargs:**

When defining a function, you can include **kwargs as a parameter. This indicates that the function can accept an arbitrary number of keyword arguments.

    def my_function(**kwargs):
        # Function body

**Passing Keyword Arguments to the Function:**

When calling the function, you can pass keyword arguments using the key=value syntax.

    my_function(arg1=value1, arg2=value2, ...)


**Accessing Keyword Arguments inside the Function:**

Inside the function, the keyword arguments are treated as a dictionary. The keys of the dictionary correspond to the argument names, and the values are the provided values.

    def my_function(**kwargs):
        for key, value in kwargs.items():
            print(key, value)

You can access the values using the dictionary methods such as `items()`, `keys()`, or `values()`.

**Example Usage:**

```python
def display_user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Example usage
display_user_info(name="John", age=30, city="New York")
```
Output:

    name : John
    age : 30
    city : New York


Using `**kwargs` provides flexibility when passing and accessing keyword arguments. It allows you to handle an arbitrary number of keyword arguments without explicitly defining them in the function signature. This can be particularly useful when you have a variable number of optional parameters or when you want to pass additional information to a function in a key-value format.

**Football Example:**

In this example, the function `display_players` accepts keyword arguments using `**kwargs`. It iterates over the provided dictionary, where each key represents a team name and the corresponding value is another dictionary that holds player details.

```python
def display_players(**kwargs):
    for team_name, team_players in kwargs.items():
        for player_name, player_details in team_players.items():
            print(f"Player details for {player_name} in team {team_name}:")
            for detail_key, detail_value in player_details.items():
                print(f"{detail_key}: {detail_value}")
            print("--------------------------------")

football_players = {
    "Real Madrid": {
        "Ronaldo": {
            "Name": "Cristiano Ronaldo",
            "Jersey Number": 7
        },
        "Benzema": {
            "Name": "Karim Benzema",
            "Jersey Number": 9
        }
    },
    "Barcelona": {
        "Messi": {
            "Name": "Lionel Messi",
            "Jersey Number": 10
        },
        "Iniesta": {
            "Name": "Andres Iniesta",
            "Jersey Number": 8
        }
    }
}

display_players(**football_players)
display_players(**{"Barcelona": {"Dica": {"Name": "Nicole Dica", "Jersey Number": 10}}})
```
Output:

    Player details for Ronaldo in team Real Madrid:
    Name: Cristiano Ronaldo
    Jersey Number: 7
    --------------------------------
    Player details for Benzema in team Real Madrid:
    Name: Karim Benzema
    Jersey Number: 9
    --------------------------------
    Player details for Messi in team Barcelona:
    Name: Lionel Messi
    Jersey Number: 10
    --------------------------------
    Player details for Iniesta in team Barcelona:
    Name: Andres Iniesta
    Jersey Number: 8
    --------------------------------
    Player details for Dica in team Barcelona:
    Name: Nicole Dica
    Jersey Number: 10
    --------------------------------

The function prints the team name and iterates over each player's dictionary to display their details. It uses nested loops (a loop inside another loop) to access the team, player, and player details.
The function is called twice: once with the football_players dictionary, which contains player information for Real Madrid and Barcelona, and once with a custom dictionary to demonstrate how the function handles different inputs.

## Automation Testing Example: Using **kwargs for Test Case Parameters
```python
def execute_test_case(test_name, **kwargs):
    print("Running test case:", test_name)
    print("Test case parameters:", kwargs)

    if test_name == "Login Test":
        # Simulating login test case
        if kwargs.get("username") == "user123" and kwargs.get("password") == "pass456":
            print("Login successful.")
        else:
            print("Login failed.")
    elif test_name == "Registration Test":
        # Simulating registration test case
        if len(kwargs.get("username", "")) > 0 and "@" in kwargs.get("email", ""):
            print("Registration successful.")
        else:
            print("Registration failed.")
    else:
        print("Unknown test case.")

# Example usage
execute_test_case("Login Test", url="https://example.com", username="user123", password="pass456")
execute_test_case("Registration Test", url="https://example.com", username="user123", email="email@example.com")

# Example usage - Negative test case
execute_test_case("Login Test", url="https://example.com", username="user123", password="wrongpass")
execute_test_case("Registration Test", url="https://example.com", username="", email="invalidemail")
```

Output:

    Running test case: Login Test
    Test case parameters: {'url': 'https://example.com', 'username': 'user123', 'password': 'pass456'}
    Login successful.
    
    Running test case: Registration Test
    Test case parameters: {'url': 'https://example.com', 'username': 'user123', 'email': 'email@example.com'}
    Registration successful.

    Running test case: Login Test
    Test case parameters: {'url': 'https://example.com', 'username': 'user123', 'password': 'wrongpass'}
    Login failed.
    
    Running test case: Registration Test
    Test case parameters: {'url': 'https://example.com', 'username': '', 'email': 'invalidemail'}
    Registration failed.

## Exceptions, Exception Handling

In Python, `exceptions` are events that occur during the execution of a program that disrupt the normal flow of instructions. They represent errors or exceptional conditions that arise while the program is running. By using `exception handling`, you can `catch` and handle these exceptions to prevent your program from crashing and provide meaningful feedback to the user.

Python provides a mechanism called `try-except` for handling exceptions. Here's the basic syntax:

    try:
        # Code that may raise an exception
    except ExceptionType1:
        # Handler for ExceptionType1
    except ExceptionType2:
        # Handler for ExceptionType2
    else:
        # Code to execute if no exceptions are raised
    finally:
        # Code that always executes, regardless of exceptions

Let's break down the parts of this syntax:

- The `try` block contains the code that might raise an exception. If any exception occurs within this block, Python immediately jumps to the appropriate `except` block.
- The `except` block catches and handles specific types of exceptions. You can have multiple `except` blocks to handle different exception types. When an exception occurs, Python checks each `except` block in order, and if the exception matches the specified type, the corresponding block is executed.
- The `else` block is optional and is executed only if no exceptions are raised in the `try` block.
- The `finally` block is also optional and is always executed, regardless of whether an exception occurred or was caught. It is typically used for cleanup operations.

_Example of non-handled exception_
    
```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 / num2
print("Result:", result)
print("Error: Division by zero!")
```

_Example of handling a specific exception_

```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
```


_Example of using else and finally blocks:_

```python

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x + y
except ValueError:
    print("Error: Invalid input!")
else:
    print("Result:", result)
finally:
    print("Program execution complete.")
```


## Automation Testing Example 
Login simulation with username and password:
```python
import time

def simulate_login(username, password):
    # Simulating login process
    print("Simulating login...")
    time.sleep(2)  # Simulating some processing time
    
    if username == "admin" and password == "password":
        print("Login successful! Welcome,", username)
    else:
        # The raise keyword in Python allows you to manually raise an exception at any point in your code.
        raise ValueError("Invalid username or password. Login failed!")

# Test the login function
try:
    # username_input = int(input("Enter your username: ")) # uncomment this to trigger this exception
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    simulate_login(username_input, password_input)
except ValueError as error:
    print("Error:", str(error))
```

## Debugging

Debugging is the process of identifying and fixing issues or bugs in your code. Here are the key features and steps for debugging in PyCharm:

**1. Setting breakpoints:** 

You can set breakpoints in your code to pause the program's execution at specific lines. To set a breakpoint, simply click in the left gutter of the code editor next to the line where you want the program to stop.

**2. Starting the debugger:**

To initiate the debugger in PyCharm, click the "Debug" button or use the keyboard shortcut (F9). This will launch your program in debug mode.

**3. Debugging controls:**

Once your program is running in debug mode, you can use various controls to step through the code, inspect variables, and navigate the program's execution. Some commonly used controls include:
- _Step Over (F8)_: Executes the current line and moves to the next line. If the current line contains a function call, it will execute the entire function without stepping into it.
- _Step Into (F7)_: Moves the debugger into the next line of code, stepping into any function call encountered.
- _Step Out (Shift + F8)_: Allows you to quickly return from the current function to its caller.
- _Resume Program (F9)_: Allows the program to continue running until the next breakpoint or completion.

**4. Inspecting variables:** 

PyCharm provides a "Variables" view that displays the values of variables in the current scope. You can inspect the values of variables by hovering over them in the code editor or by viewing them in the "Variables" view while debugging.

**5. Evaluating expressions:**

While debugging, you can evaluate expressions in the "Debug Console" to check the output or verify specific conditions. Simply enter the expression in the console and press Enter to see the result.

**6. Conditional breakpoints:** 

PyCharm allows you to set breakpoints with conditions. You can specify a condition that triggers the breakpoint only when the condition is met. Right-click on a breakpoint and choose "Edit Breakpoint" to set a condition.

**7. Debugging exceptions:** 

PyCharm can help you identify and handle exceptions efficiently. When an exception occurs during debugging, the IDE automatically stops at the line where the exception was raised, allowing you to investigate and fix the issue.












