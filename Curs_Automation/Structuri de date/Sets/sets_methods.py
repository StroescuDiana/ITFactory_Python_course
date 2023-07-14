"""
Seturi (Sets): Seturile sunt colecții neordonate și modificable de elemente unice.
Seturile sunt utile atunci când se dorește eliminarea duplicatelor și realizarea de operații matematice de set,
precum intersecția, reuniunea sau diferența.
Seturile sunt reprezentate între acolade ({}) sau utilizând funcția set().

Eliminarea duplicărilor: Seturile sunt în special utile atunci când trebuie să elimini elementele duble dintr-o colecție.
Convertind o listă într-un set și pe urma înapoi într-o listă, poți elimina ușor duplicarile.

Testarea membrilor: Seturile oferă o modalitate rapidă și eficientă de a verifica dacă un element există într-o colecție.
Datorită implementării lor interne drept tabele de adresa, seturile au o complexitate constantă pentru testarea membrilor,
făcându-le mai eficiente decât listele pentru colecții mari.

Operații de set: Seturile acceptă diferite operații matematice de set, cum ar fi uniunea, intersecția, diferența și diferența simetrică.
Aceste operații îți permit să efectuezi comparări de set și să combini sau să extragi elemente unice din diferite seturi.

Seturile sunt utile în:

-Îndepartarea duplicatelor: Prin convertirea unei liste în set și invers elimini elementele duplicate.

-Verificarea membrilor: Seturile fac verificarea rapidă dacă un element există, fiind mai eficiente decât listele prin complexitatea O(1).

-Operații de set: Uniunea, întersecția, diferența și diferența simetrică permit combinarea și extrag elemente unice din seturi.

Set Creation:
You can create a set by enclosing comma-separated elements within curly braces {}.
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

Set Elements:
Sets can only contain unique elements. Duplicate elements are automatically removed when creating or modifying a set.
my_set = {1, 2, 3, 2, 4}
print(my_set)  # Output: {1, 2, 3, 4}

Accessing Set Elements:
Sets are unordered, so you cannot access elements by index.
Instead, you can iterate over the set using a loop or check for membership using the in operator.
my_set = {1, 2, 3}
for element in my_set:
    print(element)

if 2 in my_set:
    print("2 is in the set")

Modifying a Set:
Sets are mutable, so you can add or remove elements from a set.
Adding Elements: Use the add() method to add a single element to the set.
my_set.add(4)
You can also use the update() method to add multiple elements from an iterable.
my_set.update([4, 5, 6])
Removing Elements: Use the remove() method to remove a specific element from the set.
If the element is not found, it raises a KeyError
my_set.remove(4)
Alternatively, you can use the discard() method to remove an element without raising an error if it doesn't exist in the set.
my_set.discard(5)
Set Operations:
Sets support various mathematical operations, such as union, intersection, difference, and symmetric difference.
Some commonly used set operations include:
Union: Returns a new set that contains all the unique elements from both sets.
You can use the | operator or the union() method.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
Intersection: Returns a new set that contains the common elements between two sets.
You can use the & operator or the intersection() method
intersection_set = set1 & set2
Difference: Returns a new set that contains the elements present in the first set but not in the second set.
You can use the - operator or the difference()
difference_set = set1 - set2
Symmetric Difference: Returns a new set that contains the elements present in either of the sets, but not in both.
You can use the ^ operator or the symmetric_difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)


"""
def sets_definition():
    my_set = {3, 45.7, "Ana", False}
    # pop -> stergere element din set
    # remove -> sterege un element specific din set
    # Creating a set
    fruits = {'apple', 'banana', 'orange'}
    print(fruits)  # Output: {'apple', 'banana', 'orange'}

    # Adding elements to a set
    fruits.add('kiwi')
    print(fruits)  # Output: {'apple', 'banana', 'orange', 'kiwi'}

    # Removing an element from a set
    fruits.remove('banana')
    print(fruits)  # Output: {'apple', 'orange', 'kiwi'}

    # Checking membership in a set
    print('apple' in fruits)  # Output: True
    print('grape' in fruits)  # Output: False

    # Converting a list to a set to remove duplicates
    numbers = [1, 2, 3, 3, 4, 4, 5]
    unique_numbers = list(set(numbers))
    print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

    # Set operations
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}

    # Union
    union = set1.union(set2)
    print(union)  # Output: {1, 2, 3, 4}

    # Intersection
    intersection = set1.intersection(set2)
    print(intersection)  # Output: {2, 3}

    # Difference
    difference = set1.difference(set2)
    print(difference)  # Output: {1}

    # Symmetric Difference
    symmetric_difference = set1.symmetric_difference(set2)
    print(symmetric_difference)  # Output: {1, 4}

    is_subset = set2.issubset(set1)
    print(is_subset)  # Output: True

    #  Finding Common Elements in Multiple Sets

    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {5, 6, 9, 10}

    common_elements = set1.intersection(set2, set3)
    print(common_elements)  # Output: {5}

    # Removing Duplicates from a List while Preserving Order

    numbers = [1, 2, 3, 3, 4, 4, 5]

    unique_numbers = list(dict.fromkeys(numbers))
    print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

    # Removing Common Elements from Multiple Sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {5, 6, 9, 10}

    set1.difference_update(set2, set3)
    print(set1)  # Output: {1, 2, 3}

