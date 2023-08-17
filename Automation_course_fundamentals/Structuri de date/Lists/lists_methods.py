"""
Liste (Lists): Liste sunt colecții ordonate și modificable de elemente.
Pot conține elemente de tipuri diferite și pot fi modificate prin adăugarea, ștergerea sau modificarea
elementelor existente. Listele sunt reprezentate între paranteze drepte ([]).

Lists Basics
List Creation:
You can create a list by enclosing items within square brackets [] and separating them with commas.

Accessing List Elements:
List elements can be accessed using their index, starting from 0 for the first element. You can use square brackets []

Modifying List Elements:
Lists are mutable, so you can modify individual elements by assigning new values to them using their index.

List Length:
You can find the length of a list using the len() function. It returns the number of elements in the list.

List Slicing:
You can extract a portion of a list using slicing. It allows you to specify a range of indices to extract a sublist.
sublist = my_list[1:4]  # Elements at index 1, 2, 3 will be included
print(sublist)  # Output: [2, 3, 4]

Adding Elements to a List:
You can add elements to a list using the append() method, which adds an item to the end of the list.
my_list.append(6)
You can add elements in the interior of a list in Python using: list.insert(position, value) shifts the other elem to right
You can add a sublist list.insert(index, [elements]) to insert a sublist at an index
list += [elements] to append elements to the end of the list

Removing Elements from a List:
There are several ways to remove elements from a list:
The pop() method removes and returns the element at a specific index. If no index is specified, it removes the last element.
my_list.pop(2)  # Removes the element at index 2
The remove() method removes the first occurrence of a specified value.
my_list.remove(4)  # Removes the first occurrence of 4
The del statement can be used to remove an element at a specific index or delete the entire list.
del my_list[0]  # Removes the first element
del my_list  # Deletes the entire list
Yes! You can use del to delete any variable in Python, not just lists.
It will delete the variable from the current namespace, freeing up the memory used by that variable.

List Concatenation:
You can concatenate two lists using the + operator.
It creates a new list containing all the elements from both lists. For example:
combined_list = list1 + list2

List Repetition:
You can repeat a list by using the * operator. It creates a new list with repeated elements.
repeated_list = [1, 2] * 3


"""
def lists_definition():
    my_list = [1, "doi", 3.14, True]
    # functia append() -> la final de lista
    # functia insert() -> interiorul listei
    # pop -> sterge ultimul element din lista
    # remove -> sterge element specific
    # len() -> numar elemente intr-o lista
    simple_list = [1, 2, 3, 4, 5, 6]
    mixed_list = [1, "apple", True, 3.14, [6, 7, 8]]

    """
    len(): Returns the number of elements in a list.
    append(): Adds an element to the end of the list.
    insert(): Inserts an element at a specified position in the list.
    remove(): Removes the first occurrence of a specified element from the list.
    pop(): Removes and returns the element at a specified index.
    index(): Returns the index of the first occurrence of a specified element in the list.
    count(): Returns the number of occurrences of a specified element in the list.
    sort(): Sorts the elements of the list in ascending order.
    reverse(): Reverses the order of the elements in the list.
    extend(): Appends all items from another iterable to the list.
    """

def numbered_list_methods():
    # Create a list of numbers
    numbers = [7, 3, 1, 5, 2]

    # Add an element to the end of the list
    numbers.append(4)
    print(numbers)  # Output: [7, 3, 1, 5, 2, 4]

    # Insert an element at a specified position
    numbers.insert(2, 9)
    print(numbers)  # Output: [7, 3, 9, 1, 5, 2, 4]

    # Remove the first occurrence of an element
    numbers.remove(5)
    print(numbers)  # Output: [7, 3, 9, 1, 2, 4]

    # Remove and return the element at a specified index
    popped_element = numbers.pop(3)
    print(numbers)  # Output: [7, 3, 9, 1, 2, 4]
    print(popped_element)  # Output: 1

    # Get the index of the first occurrence of an element
    index = numbers.index(3)
    print(index)  # Output: 1

    # Count the number of occurrences of an element
    count = numbers.count(7)
    print(count)  # Output: 1

    # Sort the list in ascending order
    numbers.sort()
    print(numbers)  # Output: [2, 3, 4, 7, 9]

    # Sort the list in descending order
    numbers.sort(reverse = True)
    print(numbers)  # Output: [9, 8, 5, 2, 1]

    # Reverse the order of the elements
    numbers.reverse()
    print(numbers)  # Output: [9, 7, 4, 3, 2]

    # Calculate the length of the list
    length = len(numbers)
    print(length)  # Output: 5

    my_list = [1, 2, 3]
    another_list = [4, 5, 6]
    my_list.extend(another_list)

def string_list_methods():
    text = "This is a fairly long string that will test some list methods."

    # Split the string into a list of words
    words = text.split()
    print(words)

    # Get every second word from the list
    every_second = words[::2]
    print(every_second)

    # Sort the list of words
    words.sort()
    print(words)

    # Reverse the list of words
    words.reverse()
    print(words)

    # Join the words into a sentence with '-' as separator
    new_text = '-'.join(words)
    print(new_text)

    # Capitalize every word in the list
    # words = [word.capitalize() for word in words] -> expression is used before the for statement
    capitalized_words = []

    for word in words:
        # Capitalize the word and append it to the capitalized_words list
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)

    # print(words)
    print(capitalized_words)

    # Count the number of 'is' in the text
    print(text.split('is').count('is'))

    # Replace the first 'long' with 'very long'
    words[words.index('long')] = 'very long'
    print(words)

    # Insert 'extremely' before 'fairly'
    words.insert(words.index('fairly'), 'extremely')
    print(' '.join(words))

    # Remove the last 3 words
    words = words[:-3]
    print(' '.join(words))
