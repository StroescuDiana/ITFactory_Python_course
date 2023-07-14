'''
!!!!! haha_upps = snake case
!!!!! hahaUpps = camel case


my_list = [1, 2, 3]
other_list = []
doubles = [x * 2 for x in my_list] # sintaxa este un list comprehension | DOAR in Python
print(doubles)

# syntactic sugar
for i in my_list:
    double = i * 2
    other_list.append(double)


#1. Declarati o lista cu elemente multitype
lista = [1, 2, "Alina", 4, "mere", True, 4.20]

#2. Declarati o lista goala
empty_list = []
lista2 = list()

#3. Accesati orice element din lista pe baza de index
#   list slicing = se poate face ca sa extragi mai multe numere sau sa extragi pe baza de index
#   [start:STOP:step] stop = parametru obligatoriu
# print(lista[0])
# print(lista[1:])

numbers = list(range(1, 11))
print(numbers[1::2])
print(numbers[::-1])

#4. Accesati pozitia unui element din lista pe baza functiei index
#   index() este utilizata pentru a returna indexul corespunzator
#   primei aparitii a unei valori intr-o lista
#parametri: value(mandatory), start(optional), end(optional)
print(numbers.index(3))



#5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
numbers = list(range(1, 11))
#   append() = este utilizata pentru a adauga un element la sfarsitul unei liste existente
numbers.append(20)

#   insert() = insereaza un element intr-o lista la un index specificat
numbers.insert(1, 999)
print(numbers)

# numbers.extend(["mere", "pere", "banane"])
# print(numbers)

# pentru a insera mai multe elemente la un index specific
lista = [1, 2, "Alina", 4, "mere", True, 4.20]
lista[2:2] = [2.1, 2.2, 2.3]
print(lista)


#6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
lista.pop()
lista.pop(3)
print(lista)

lista.remove(4)
print(lista)

#7. Numarati elementele dintr-o lista folosind functia len()
print(len(lista))


#8. Numarati de cate ori apare un anumit element in lista folosind functia count()
lista.append("Alina")
print(lista)
#print(lista.count("Alina"))


#10. Sortati lista folosind functia sort()
#
# numbers.sort()
# print(numbers)
#

#11. Inversati continutul listei folosind functia reverse()
print(numbers)
numbers.reverse()
print(numbers)

#12. Stergeti toate elementele din lista folosind functia clear()
#   list.clear()

#12. Parcurgeti o lista si printati toate elementele din aceasta folosind pe rand for, while si for each
# for num in numbers:
#     print(num)

# i = 0
# while i <= len(numbers):
#     print(f"Numarul curent este: {numbers[i]}")
#     i += 1
'''





#1. Declarati un tuplu
names = ("Diana", "Felix", "Teodor", "Diana", "Elena", "Adi")

#2. Declarati un tuplu gol
my_tuple = tuple()

#3. Accesati orice element din tuplu pe baza de index
print(names[1:])
# indexii negativi se folosesc pentru a accesa indexii din coada
print(names[-1])

# DOAR afiseaza ordine inversa
print(names[::-1])

#4. Accesati pozitia unui element din lista pe baza functiei index()
#print(names.index("Diana"))

#5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
print(names.count("Diana"))

#6. Folositi functia index() pentru a verifica pozitia la care se afla un anumit element in tuplu
#assert names.index("Adi") == 3, "Nu se afla la pozitia specificata"
#   arrange, act, assert

cars = ("Audi", "BMW", "Toyota", "Miata", "Dacia")

element = "Toyota"
index = cars.index(element)

expected_index = 2

assert index == expected_index, f"Elementul {element} nu se afla la pozitia asteptata."
print(f"Elementul {element} se afla la pozitia {index} in tuple.")


# #7. Incercati sa modificati un element din tuplu si observati rezultatele
# cars[0] = "Volvo"  #Va genera o eroare intrucat tuplul nu suporta modificari
# print(cars)

'''
#1. Declarati un set
my_set = {1, 2, 3}

#2. Declarati un set gol
empty_set = set()
print(type(empty_set))

#3. Adaugati un element nou in set folosind functia add()
my_set.add(4)
print(my_set)

#4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele

removed_element = my_set.pop()
print(removed_element)

my_set.remove(3)
print(my_set)
'''

#5. Verificati daca un set este o subdiviziune a unui alt set (subset)

angajati = {"Alina", "Vlad", "George", "Bogdan", "Rares"}
vanzari = {"Vlad", "George", "Bogdan"}

assert vanzari.issubset(angajati), f"Persoanele urmatoare {vanzari} nu sunt angajate."
print(f"Urmatorii colegi fac parte din departamentul de vanzari: {', '.join(vanzari)}")


#6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)
print(angajati.issuperset(vanzari))

#7. Verificati care sunt elementele comune intre doua seturi (intersection)
angajati_comuni = angajati.intersection(vanzari)
print(angajati_comuni)









