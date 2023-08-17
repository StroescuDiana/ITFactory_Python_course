"""
Tuple: Tuple sunt colecții ordonate și imodificabile de elemente.
Similar cu liste, pot conține elemente de tipuri diferite, dar diferența majoră este că
tuplele nu pot fi modificate după ce au fost create.
Tuplele sunt reprezentate între paranteze rotunde (()).

They are similar to lists but have some key differences.
Tuple Creation:
You can create a tuple by enclosing comma-separated elements within parentheses ().
my_tuple = (1, 2, 3)
Alternatively, you can create a tuple without parentheses, using just commas.
my_tuple = 1, 2, 3
Tuple Elements:
Tuples can contain elements of different data types, including numbers, strings, booleans, and even other tuples.
Elements within a tuple are ordered and immutable, meaning they cannot be changed once the tuple is created.
Accessing Tuple Elements:
You can access tuple elements using their indices, starting from 0 for the first element.
You can use square brackets [] with the index inside them.
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 3 (last element)
Tuple Packing and Unpacking:
Tuple packing refers to creating a tuple by assigning values to a comma-separated sequence of variables.
my_tuple = 1, 2, 3
Tuple unpacking refers to assigning the elements of a tuple to multiple variables in a single assignment statement.
a, b, c = my_tuple
Tuple packing and unpacking are often used together to swap variable values
a = 1
b = 2
a, b = b, a
Modifying Tuple Elements:
Tuples are immutable, so you cannot change individual elements once a tuple is created.
However, you can create a new tuple with modified or added elements.
Tuple Methods:
Tuples have a few built-in methods, including:
count(): Returns the number of occurrences of a specified value in the tuple.
index(): Returns the index of the first occurrence of a specified value in the tuple.
Tuple Operations:
Tuples support various operations, including concatenation, repetition, and slicing, similar to lists.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Slicing
sub_tuple = combined_tuple[1:4]
print(sub_tuple)  # Output: (2, 3, 4)

In Python, tuples are immutable, which means you cannot modify them once they are created.
Therefore, you cannot directly add or remove elements from a tuple.
 However, you can create a new tuple by concatenating existing tuples with the desired element
my_tuple = (1, 2, 3)

# Adding an element by creating a new tuple
new_tuple = my_tuple + (4,)
print(new_tuple)  # Output: (1, 2, 3, 4)

"""
def tuples_definition():
    # my_tuple = (1, 2, 3, "patru", "cinci")
    # se poate face orice operatie de accesare de elemente
    # dar nici o operatie de adaugare, stergere sau modificare

    # Creation of Tuples
    my_tuple = (1, 2, 3)  # Creating a tuple using parentheses

    another_tuple = tuple([4, 5, 6])  # Creating a tuple using the tuple() function

    # Immutability of Tuples
    # my_tuple[0] = 10  # Uncommenting this line will result in a TypeError as tuples are immutable

    # Accessing Elements
    print(my_tuple[0])  # Output: 1 - Accessing the first element of the tuple
    print(my_tuple[-1])  # Output: 3 - Accessing the last element of the tuple

    # Tuple Operations
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5)

    concatenated_tuple = tuple1 + tuple2  # Concatenating two tuples
    repeated_tuple = tuple1 * 3  # Repeating a tuple
    sliced_tuple = concatenated_tuple[1:4]  # Slicing a tuple

    print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5)
    print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
    print(sliced_tuple)  # Output: (2, 3, 4)

    # Tuple Methods
    my_tuple = (1, 2, 3, 2, 4, 2)

    print(my_tuple.count(2))  # Output: 3 - Counting the occurrences of a value in the tuple
    print(my_tuple.index(4))  # Output: 4 - Finding the index of a value in the tuple

    # Use Cases for Tuples
    # Tuples as immutable collections of related values
    coordinates = (10, 20)
    rgb_color = (255, 0, 0)

    # Returning multiple values from a function using a tuple
    def get_name_and_age():
        name = "John"
        age = 25
        return name, age

    name, age = get_name_and_age()
    print(name)  # Output: John
    print(age)  # Output: 25

    # Unpacking a tuple
    x, y, z = (10, 20, 30)
    print(x)  # Output: 10
    print(y)  # Output: 20
    print(z)  # Output: 30

def tuples_imutability_exception():
    # Creating a tuple with a mutable object (list)
    my_tuple = ([1, 2, 3], 'Hello', [4, 5, 6])

    # Modifying the list within the tuple
    my_tuple[0].append(4)
    my_tuple[0][1] = 10

    # Modifying the list outside the tuple
    nested_list = my_tuple[0]
    nested_list.append(5)

    print(my_tuple)  # Output: ([1, 10, 3, 4, 5], 'Hello', [4, 5, 6])

