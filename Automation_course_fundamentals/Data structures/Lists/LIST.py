def numbered_list():
    numbers = [1, 2, 7, 3, 4, 5, 6, 7, 8, 9, 7]

    #add an element to the end of the list
    numbers.append(10)

    # add an element at a specific position
    numbers.insert(11, 11) # prima data pozitia, apoi elementul

    # remove the first occurrence of an element
    numbers.remove(11)
    print(numbers)
    #remove & return the element of a specific index/position
    print(numbers)
    pop_element = numbers.pop(9)
    print(pop_element)

    # get the index of the first occurrence of an element
    print(numbers)
    index = numbers.index(5)
    print(index)

    # count the number of occurrences of an element
    count = numbers.count(7)
    print(f'Cifra 7 apare de: {count} ori')

    # sort the list in ascending order
    numbers.sort()
    print(numbers)

    # sort the list in descending order
    numbers.sort(reverse = True)
    print(numbers)

    # schimba ordinea valorilor pe baza indexilor
    numbers.reverse()
    print(numbers)

    # calculate the lenght of the list
    lenght = len(numbers)
    print(lenght)

    my_list = [1, 2, 3]
    another_list = [4, 5, 6]
    my_list.extend(another_list)  # extend() adauga elementele dintr-o lista la alta
    print(my_list)


def string_list_methods():
    text = "Acesta este un text lung pentru a exersa metode pe liste"

    cuvinte_separate = text.split()  # split() separa elementele dintr-un string si le pune intr-o lista
    print(cuvinte_separate)

    every_second_word = cuvinte_separate[::2]
    print(every_second_word)

    # sortam crescator
    cuvinte_separate.sort()
    print(cuvinte_separate)

    # sortam descrescator
    cuvinte_separate.sort(reverse = True)
    print(cuvinte_separate)

    # reverse
    cuvinte_separate.reverse()
    print(cuvinte_separate)

    new_text = ' '.join(cuvinte_separate)
    print(new_text)


#---------------------------------------------
# instructiuni repetitive
    # pentru un numar de ori/ iteratii, o sa facem o anumita actiune

text = "Acesta este un text lung pentru a exersa metode pe liste"
cuvinte_separate_ = text.split()

capitalized_words = []

for cuvant in cuvinte_separate_:
    cap_word = cuvant.capitalize()
    print(cap_word)
    capitalized_words.append(cap_word)

print(capitalized_words)




# if __name__ == '__main__':
#     numbered_list()
#     string_list_methods()