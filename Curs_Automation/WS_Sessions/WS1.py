'''
CTRL + ALT + L -> formatare cod
CTRL + / -> comentariu
'''

# o variabila = o cutie in care se pot stoca date
'''
nr_int = 3
nr_float = 5.9
string = "Salut Lume"
another_string = '123'
angajat = True

print(type(nr_int))
print(type(nr_float))
print(type(string))
print(type(angajat))
print(str(type(nr_int)) + " " + str(type(nr_float)) + " " + str(type(string)) + " " + str(type(angajat)))

nr_float = round(nr_float)
print(nr_float)

print(int(another_string)) # se poate converti un string in int
print(int(string)) # nu se poate converti un string format din litere in int
print(int(angajat)) # True = 1, False = 0

print(not angajat) # negarea unei variabile booleane
'''

def concatenare():
    name = "John"
    age = 30
    occupation = "engineer"
    print("Person 1: Name =", name, ", Age =", age, ", Occupation =", occupation) # concatenare

    city = "New York"
    population = 8_500_000
    area = 302.6
    print("City: {}, Population: {}, Area: {} sq km".format(city, population, area)) # concatenare prin format

    nr_int = 3
    nr_float = 5.9
    angajat = True
    print(f'Numarul meu este {nr_int} si numarul meu float este {nr_float}') # concatenare prin f-string
    print(f'Salut Lume! Astazi am 123 de lei in cont si am fost angajat: {angajat}')

#concatenare()


def input_tastatura():
    nume = input("Introduceti numele: ")
    prenume = input("Introduceti prenumele: ")
    print("Numele complet are ", len(nume) + len(prenume), " caractere")

#input_tastatura()

def aria_dreptunghi():
    lungime = float(input("Introduceti lungimea: "))
    latime = float(input("Introduceti latimea: "))
    print("Aria dreptunghiului este: ", lungime * latime)

#aria_dreptunghi()

def coral(coral_text):
    print(coral_text.count("the")) # il include si pe "the" din "either"
    print(coral_text.count(" the ")) # il include doar pe "the"
    coral_text = coral_text.replace(" the ", " <3 ")
    print(coral_text)

#coral("Coral is either the stupidest animal or the smartest rock")

'''
# verifica daca stringul este format doar din cifre
numere = "1D"
print(numere.isdigit()) # False
assert numere.isdigit() == True, "Stringul nu este format doar din cifre"

def suma():
    return 2 + 3
assert suma() == 4, "Suma nu este 4"
'''

#Ex_1(dificultate medie) Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
def ex1_dificultate_medie():
    string_impar = input("Introduceti un string de dimensiune impara: ")
    if len(string_impar) % 2 == 1:
        index_caracter_mijloc = len(string_impar) // 2 # // = impartire intreaga(fara zecimale), se face numerotarea de la 0
        print(f'Caracterul din mijloc este: {string_impar[index_caracter_mijloc]}')
    else:
        print(f"Stringul {string_impar} este de dimensiune para.")

#ex1_dificultate_medie()

'''
def isPalindrom(string):
    string = string.lower().replace(" ", "")
    reversed_string = string[::-1]
#---returnam o valoare bool -> True sau False
    bool_rezultat = (string == reversed_string)
    return bool_rezultat

palindrom = "Radar"
not_palindrom = "Python"

assert isPalindrom(palindrom) == True, "Nu este palindrom"
assert isPalindrom(not_palindrom) == True, "Nu este palindrom"
'''


# Ex_3(dificultate medie) - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

def ex3_dif_medie():
    string = input("Introduceti text: ")
    cuvinte = string.split()
    cuvant_1 = cuvinte[0]
    cuvant_2 = cuvinte[1]
    print(f"Cuvantul 1 este: {cuvant_1} si cuvantul 2 este: {cuvant_2}")


#ex3_dif_medie()


# Ex_4(dificultate medie): alabala portocala/ wordwordword
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

def ex4_dif_medie():
    string = input("Introduceti text: ")
    primul_caracter = string[0]
    result_string = primul_caracter + string[1:-1].replace(primul_caracter, primul_caracter.upper()) + string[-1]
    # adaugam + string[-1] pentru ca in slicing ultimul caracter nu este inclus!
    print(result_string)


#ex4_dif_medie()


#Ex_15 - citeste un user de la tastatura, citeste o parola.
# Afiseaza: 'Parola pt user x este ***** si are x caractere

def ex_15():
    username = input("username: ")
    password = input("password: ")
    hidden_password = "*" * len(password)
    print(f"Usernameul este {username} si parola este {hidden_password} si are {len(password)}.")


#ex_15()


#Ex_6 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi,
# afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale)
# sau oarecare (nicio latura nu e egala).
def tip_triunghi():
    x = int(input("Introduceti lungimea primei laturi: "))
    y = int(input("Introduceti lungimea celei de-a doua laturi: "))
    z = int(input("Introduceti lungimea celei de-a treia laturi: "))
    if x == y == z:
        print("Triunghiul este echilateral.")

    elif x == y or y == z or x == z:
        print("Triunghiul este isoscel.")

    else:
        print("Triunghiul este oarecare.")


#tip_triunghi()


# Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este numele filmului vostru preferat.
# Daca da, atunci printati pe ecran: “Acesta este filmul meu preferat”. In caz contrar printati pe ecran:
# Din pacate nu este filmul meu preferat”

def favourite_movie(film_preferat_Diana):
    movie = input("Movie's name: ")
    if movie == film_preferat_Diana:
        print("Acesta este filmul meu preferat.")
    else:
        print("Din pacate nu este filmul meu preferat.")

#favourite_movie("Interstellar")


def favourite_movie_1(film_preferat_Diana):
    movie = input("Movie's name: ")
    if movie == film_preferat_Diana:
        return "Acesta este filmul meu preferat."
    else:
        return "Din pacate nu este filmul meu preferat."

rezultat = favourite_movie_1("Interstellar") # Declaram o variabila care stocheaza mesajul
print(rezultat)
# print(favourite_movie_1("Interstellar"))
'''
Tema: de facut restul exercitiilor 
https://docs.google.com/presentation/d/14iBpCnwungsnH1CkM7_z7rABg9WYFhQM/edit#slide=id.g245de6dc469_0_12
'''