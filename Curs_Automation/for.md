# FOR
The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It allows you to perform a set of actions for each element in the sequence. 

*The general syntax of a for loop in Python is as follows:*

```python
sequence = []
for element in sequence:
    # Code block to be executed for each element
    pass # adica nu executa nici o instrucitune, blocul este gol
```


### Range
In Python, range() is a built-in function that generates a sequence of numbers. It is commonly used to create a sequence of integers that can be iterated over in loops, such as for loops. 
The range() function returns an immutable sequence of numbers based on the specified start, stop, and step values.

*The general syntax of range is:*

    range(start, stop, step)


**Range definition and structure:**
- range(start, stop, step)
- start (optional): It specifies the starting point of the sequence. If not provided, it defaults to 0.
- stop: It specifies the ending point of the sequence (exclusive). This value is required.
- step (optional): It specifies the difference between each number in the sequence. If not provided, it defaults to 1.

```python
for num in range(1, 6):
    print(num) # 1 2 3 4 5
```

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        
"""
Output:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
"""
```
### Enumerate

**Enumerate definition and structure:**
In Python, enumerate() is a built-in function that provides an elegant way to iterate over a sequence while keeping track of the index and the corresponding element at the same time. The enumerate() function returns an iterator that generates pairs of index-element tuples.

*The syntax of the enumerate() function is as follows:*
```python
sequence = []
enumerate(sequence, start=0)
```
Here, sequence is the iterable object that you want to iterate over, and start (optional) is the value of the index from which the enumeration starts. By default, start is set to 0.

The enumerate() function generates tuples in the form (index, element) for each element in the sequence. 
The index represents the position of the element in the sequence, starting from the specified start value (or 0 if not provided), and the element represents the corresponding value from the sequence.

**Example of enumerate:**
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 1, Fruit: apple
# Index: 2, Fruit: banana
# Index: 3, Fruit: cherry

```

### Other examples of for usage: 
```python
for i in range(1, 102):
    print(f"Dalmatianul curent este {i}")
```

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

```python
message = "Hello"
for char in message:
    print(char)
```

```python
student_scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90}
for name, score in student_scores.items():
    print(name, score)
```

**Using break in a for loop:**

```python
# Using break and continue in a for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Using break in a for loop:")
for num in numbers:
    if num == 5:
        break  # Exit the loop when num equals 5
    print(num)
```
**Using continue in a for loop:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nUsing continue in a for loop:")
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers and continue to the next iteration
    print(num)
```

**Using break in a for-each loop:**
```python
fruits = ["apple", "banana", "cherry", "durian", "elderberry"]

print("Using break in a for-each loop:")
for fruit in fruits:
    if fruit == "durian":
        break  # Exit the loop when fruit is "durian"
    print(fruit)


```
**Using continue in a for-each loop:**
```python
fruits = ["apple", "banana", "cherry", "durian", "elderberry"]

print("\nUsing continue in a for-each loop:")
for fruit in fruits:
    if fruit.startswith("b"):
        continue  # Skip fruits starting with "b" and continue to the next iteration
    print(fruit)
```
**Another enumerate example:**

Here's an example where the first element of a for loop is the iterator itself:
```python
fruits = ["apple", "banana", "cherry"]

# Here's an example where the first element of a for loop is the iterator itself:
for index, fruit in enumerate(fruits):
    print("Index:", index)
    print("Fruit:", fruit)
    print("---")
```
**Another range example:**

```python
my_list = ["apple", "banana", "cherry"]

for i in range(len(my_list)):
    print("Index:", i)
    print("Element:", my_list[i])
    print("---")

```
In this example, the range(len(my_list)) generates a sequence of indices corresponding to the elements of my_list. The len(my_list) function returns the length of the list, and range() creates a range of integers from 0 to len(my_list) - 1.
Then, the for loop iterates over these indices, and my_list[i] is used to access the element at the current index.
By combining range(len(my_list)) with my_list[i], you can access the elements of my_list.


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

**Function for continue statement example:**
```python
def continue_example():
    suma_1 = 0
    for i in range(0, 11):
        if i % 2 == 0:
            continue
        suma_1 += i
    print(f"Suma numerelor impare de la 0 la 10 este: {suma_1}")

continue_example()
```


**Running test cases using for simulation:**
```python
def for_test_case_example():
    test_cases = ["Test Case 1", "Test Case 2", "Test Case 3", "Test Case 4", "Test Case 5"]

    for case in test_cases:
        print("Running test case:", case)

        # Simulating test execution
        if case == "Test Case 3":
            print("Test case failed!")
            break

        if case == "Test Case 2":
            print("Test case skipped!")
            continue

        print("Test case passed!")

    print("End of test execution.")
    
for_test_case_example()
```

