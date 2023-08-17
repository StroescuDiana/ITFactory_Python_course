# WHILE 
### The syntax of a while loop in Python is as follows:

```python
condition = True
while condition:
    # Code to be executed while the condition is True
    pass
```
Here, condition is an expression that evaluates to either True or False. The loop will continue executing the code block as long as the condition remains True. Once the condition becomes False, the loop will terminate, and the program will continue with the next line of code after the loop.

### Simple while loop: This is the basic form of a while loop.

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```
In this example, the loop will continue executing as long as the count variable is less than 5. The count variable is incremented by 1 in each iteration, and the current value of count is printed.

**Iterating an index with while:**
```python
def first_while():
    i = 1
    while i <= 101:
        print(f"Dalmatianul curent este: {i}")
        i += 1

first_while()
```
**Iterating through each element in a list:** <br>

```python
fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
```
In this example, the while loop iterates over each element in the fruits list using an index variable index.
The loop continues until the index reaches the length of the list.

**Iterating over each element in a tuple:** <br>
```python
numbers = (1, 2, 3, 4, 5)
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
```
Here, the while loop iterates over each element in the numbers tuple using an index variable. The loop continues until the index reaches the length of the tuple.

**Iterating over each key-value pair in a dictionary:**
```python
student_scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90}
keys = list(student_scores.keys())
index = 0
while index < len(keys):
    name = keys[index]
    score = student_scores[name]
    print(name, score)
    index += 1
```
Here, the while loop iterates over each key-value pair in the student_scores dictionary using an index variable. The loop continues until the index reaches the length of the list of keys.

### Break statement:
The break statement is used to exit or terminate the loop prematurely.
When a break statement is encountered inside a loop, the loop is immediately terminated, and the program execution continues with the next statement outside the loop. This allows you to exit the loop based on a certain condition.
```python
def break_statement():
    count = 0
    while True:
        count += 1
        if count > 5:
            break  # Exit the loop when count exceeds 5
        print(count) # 1 2 3 4 5
        
break_statement()
```
In the above example, the while loop continues indefinitely (since the condition is always True), but when count exceeds 5, the break statement is encountered, and the loop is terminated. The program execution continues with the next statement after the loop.

**Function for break statement example:**
```python
def break_example():
    date_plata_facturi = [1, 10, 15, 20, 25, 30]
    data_plata_factura = 15

    for i in range(len(date_plata_facturi)):
        print(
            f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare. Cumpara chibrituri")
        if date_plata_facturi[i] == data_plata_factura:
            print(f"Factura a fost platita in ziua de {date_plata_facturi[i]}, nu mai mananci la lumanare")
            break
break_example()
```
In the above function, the break_example() function represents the code that utilizes the break statement. 
It iterates over the date_plata_facturi list and checks if the current element matches the data_plata_factura. 
When a match is found, it prints the corresponding message and exits the loop using the break statement.

### Continue statement:
The continue statement is used to skip the remaining part of the loop for the current iteration and proceed to the next iteration. When a continue statement is encountered inside a loop, the loop jumps to the next iteration without executing the remaining code below the continue statement for the current iteration.
```python
def continue_statement():
    count = 0

    while count < 5:
        count += 1
        if count == 3:
            continue  # Skip the rest of the loop for count=3
        print(count)
        # 1 2 4 5

continue_statement()
```
The above code demonstrates the usage of the continue statement within a while loop. When the loop encounters the value of count equal to 3, the continue statement is triggered, causing the remaining code in that iteration to be skipped. As a result, the number 3 is not printed, and the loop proceeds to the next iteration.

**Function for continue statement example:**
```python
def continue_example():
    suma_1 = 0
    for i in range(0, 11):
        if i % 2 == 0:
            continue
        suma_1 += i
    print(f"Suma numerelor impare de la 0 la 10 este: {suma_1}")
```
In the above function, the continue_example() function demonstrates the code that utilizes the continue statement. 
It calculates the sum of odd numbers from 0 to 10. When an even number is encountered (if i % 2 == 0), the continue statement is triggered, skipping the rest of the loop for that iteration. 
As a result, only odd numbers contribute to the sum.

# Problems

### Guess the number between a specific range
```python
import random

def guess_the_number():
    # Generate a random number within a specified range
    min_number = 1
    max_number = 20
    target_number = random.randint(min_number, max_number)

    # Initialize variables
    guess = None
    attempts = 0

    # Play the game
    while guess != target_number:
        guess = int(input("Guess the number between {} and {}: ".format(min_number, max_number)))
        attempts += 1

        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")

    print("Congratulations! You guessed the number {} correctly in {} attempts.".format(target_number, attempts))

# function call to execute the code
guess_the_number()
```

### Guess the favorite film, only one chance

```python
def favorite_film():
    favorite_film = "Inception"  # Your favorite film's name


    film_name = input("Introduceți numele unui film: ")

    if film_name == favorite_film:
        print("Acesta este filmul meu preferat.")
    else:
        print("Din păcate nu este filmul meu preferat.")
        
# function call to execute the code
favorite_film()
```
### Guess the favorite film mutiple chances

```python
def favorite_film_form_input():
    # List of film names
    films = ["Avatar", "Titanic", "Jurassic Park", "The Godfather", "Inception", "Interstellar"]

    attempts = 0

    while True:
        favorite_film = input("Introduceți numele unui film preferat: ")
        attempts += 1

        for film in films:
            if film == favorite_film:
                print("This is my favorite movie !")
                break
        else:
            print("This is NOT one of my favorite movies !")
            continue

        break

    print("You guessed the favorite film '{}' correctly in {} attempts.".format(favorite_film, attempts))
    
# function call to execute the code
favorite_film_form_input()
```

### Computer tries to guess the favorite film
```python
import random

def favorite_film_computer_guess():
    favorite_film = "Inception"  # Your favorite film's name

    # List of film names
    films = ["Avatar", "Titanic", "Jurassic Park", "The Godfather", "Inception", "Interstellar"]

    guess = None
    attempts = 0

    while guess != favorite_film:
        guess = random.choice(films)
        attempts += 1

        print("Computer's guess: {}".format(guess))

        guess_index = films.index(guess)
        favorite_index = films.index(favorite_film)

        if guess_index < favorite_index:
            print("Higher!")
        elif guess_index > favorite_index:
            print("Lower!")

    print("Computer guessed the favorite film '{}' correctly in {} attempts.".format(favorite_film, attempts))

# function call to execute the code
favorite_film_computer_guess()
```


```python
# To be continued
```