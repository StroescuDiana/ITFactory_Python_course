"""
Dicționarele sunt colecții neordonate de perechi cheie-valoare. Ele permit accesarea rapidă a valorilor folosind chei unice.
Dicționarele sunt reprezentate între acolade ({}) și perechile cheie-valoare sunt separate prin doi puncte (:).

Creating a Dictionary:
To create a dictionary, you can use curly braces {} and separate the keys and values using a colon :
# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
You can also use the dict() constructor to create a dictionary:
# Creating a dictionary using dict()
my_dict = dict(name="John", age=25, city="New York")
Accessing Dictionary Values:
You can access the values in a dictionary by referencing the keys.
# Accessing dictionary values
print(my_dict["name"])  # Output: John
print(my_dict["age"])  # Output: 25
print(my_dict.get("city"))  # Output: New York
If you try to access a key that doesn't exist in the dictionary, it will raise a KeyError.
However, using the get() method allows you to handle this situation more gracefully by returning a default value
(or None if not provided) instead of raising an error.
Modifying Dictionary:
Dictionaries are mutable, meaning you can modify their values and add or remove key-value pairs.
Here are some common operations:
# Modifying dictionary values
my_dict["age"] = 26  # Updating the value of the "age" key
my_dict["city"] = "San Francisco"  # Updating the value of the "city" key

# Adding a new key-value pair
my_dict["occupation"] = "Software Engineer"

# Removing a key-value pair
del my_dict["age"]  # Deleting the "age" key and its value

Dictionary Methods:
Python provides various useful methods for working with dictionaries. Here are a few commonly used ones:
keys(): Returns a list of all the keys in the dictionary.
values(): Returns a list of all the values in the dictionary.
items(): Returns a list of key-value pairs as tuples.
len(): Returns the number of key-value pairs in the dictionary.
clear(): Removes all the key-value pairs from the dictionary.

print(my_dict.keys())  # Output: ['name', 'city', 'occupation']
print(my_dict.values())  # Output: ['John', 'San Francisco', 'Software Engineer']
print(my_dict.items())  # Output: [('name', 'John'), ('city', 'San Francisco'), ('occupation', 'Software Engineer')]
print(len(my_dict))  # Output: 3

my_dict.clear()  # Clears all the key-value pairs

Iterating Over a Dictionary:
You can loop over a dictionary to access its keys, values, or both.
# Iterating over a dictionary
for key in my_dict:
    print(key, my_dict[key])

# Iterating over keys and values simultaneously
for key, value in my_dict.items():
    print(key, value)

# Update dictionaries
dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "occupation": "Engineer"}

# Updating dict1 with the key-value pairs from dict2
dict1.update(dict2)

# Printing the updated dictionary
print(dict1)

Here's an example that demonstrates accessing a key that doesn't exist in a dictionary, resulting in a KeyError

my_dict = {"name": "John", "age": 25, "city": "New York"}

# Trying to access a non-existent key
print(my_dict["occupation"])

-> KeyError: 'occupation'

my_dict = {"name": "John", "age": 25, "city": "New York"}

# Using the get() method to access a key
print(my_dict.get("occupation"))

-> None

"""
def dictionaries():
    # my_dictionary = {"cheie1": "valoare1", "cheie2": "valoare2", "cheie3": "valoare3"}
    # ordonate si mutabile, putem adauga, sterege, modifica valori din interiorul unui dictionar
    # accesarea elementelor se face prin intermediul cheilor
    # adaugarea elementelor in dictionar se face prin functia update sau
    # prin incercarea de a modifica un element cu o cheie inexistenta

    """
    Dictionaries in Python are unordered collections of key-value pairs.
    They are also known as associative arrays, hash maps, or hash tables in other programming languages.
    Dictionaries are widely used due to their ability to store and retrieve data efficiently based on unique keys.
    """

    my_dictionary = {"nume": "Ana", "prenume": "Anton", "durata_angajare": 2, "varsta": 45.6, "inca_angajata": True}

    # Creating a dictionary
    student = {
        'name': 'John',
        'age': 20,
        'grade': 'A'
    }

    # Accessing dictionary values
    print(student['name'])  # Output: John
    print(student['age'])  # Output: 20
    print(student['grade'])  # Output: A

    # Modifying dictionary values
    student['grade'] = 'B'
    print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'B'}

    """
    Dictionaries provide various built-in methods to manipulate and retrieve data. Here are some commonly used methods:
    keys(): Returns a view object of all the keys in the dictionary.
    values(): Returns a view object of all the values in the dictionary.
    items(): Returns a view object of all the key-value pairs in the dictionary.
    get(): Retrieves the value associated with a given key, or a default value if the key is not found.
    pop(): Removes and returns the value associated with a given key.
    update(): Updates the dictionary with key-value pairs from another dictionary or iterable.
    clear(): Removes all the key-value pairs from the dictionary.
    len(): Returns the number of key-value pairs in the dictionary.
    """

    # Using dictionary methods
    print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])
    print(student.values())  # Output: dict_values(['John', 20, 'B'])
    print(student.items())  # Output: dict_items([('name', 'John'), ('age', 20), ('grade', 'B')])
    print(student.get('name'))  # Output: John
    student.pop('age')
    print(student)  # Output: {'name': 'John', 'grade': 'B'}

    """
    You can iterate over a dictionary using a for loop. By default, the loop iterates over the keys of the dictionary. 
    To access both the keys and values, you can use the items() method.
    """
    # Iterating over a dictionary
    for key in student:
        print(key)  # Output: name, age, grade
        print(student[key])  # Output: John, 20, B

    for key, value in student.items():
        print(key, value)  # Output: name John, age 20, grade B


def dictionary_methods():
    # len(): Returns the number of key-value pairs in the dictionary.
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    print(len(my_dict))  # Output: 3

    # keys(): Returns a list-like object containing all the keys in the dictionary.
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    print(my_dict.keys())  # Output: dict_keys(['apple', 'banana', 'orange'])

    # values(): Returns a list-like object containing all the values in the dictionary.
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    print(my_dict.values())  # Output: dict_values([3, 5, 2])

    # items(): Returns a list-like object containing all the key-value pairs as tuples.
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    print(my_dict.items())  # Output: dict_items([('apple', 3), ('banana', 5), ('orange', 2)])

    # get(): Returns the value associated with the specified key.
    # If the key is not found, it returns a default value (or None if not specified).
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    print(my_dict.get('apple'))  # Output: 3
    print(my_dict.get('grape'))  # Output: None
    print(my_dict.get('grape', 'Not found'))  # Output: 'Not found'

    # update(): Updates the dictionary with the key-value pairs from another dictionary or an iterable.
    my_dict = {'apple': 3, 'banana': 5}
    new_data = {'orange': 2, 'grape': 4}
    my_dict.update(new_data)
    print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 4}

    # pop(): Removes the item with the specified key and returns its value.
    # If the key is not found, it raises a KeyError (or returns a default value if specified).
    my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
    value = my_dict.pop('banana')
    print(value)  # Output: 5
    print(my_dict)  # Output: {'apple': 3, 'orange': 2}
