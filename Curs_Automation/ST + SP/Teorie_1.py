"""
Comentarii multiple
Codul acesta nu se executa
"""

# Afiseaza in consola Hello World!
print("Hello World!")
# Principalele tipuri de date si declararea lor in Python
x = 5        # Integer / int
y = 5.0      # Float / float
name = "John" # String / str
is_true = True  # Boolean / bool
is_false = False # Boolean

sunt_la_curs, imi_place_supa = "da", "nu"
imi_place_python = "DA"
Imi_place_python = "NU"

# Constanta
SUNT_INSCRIS_LA_CURS = True

# Inglobarea variabilelor in print prin concatenare
nume = "Ion Popescu" # string
an_nastere = 1963 # int
salariu = 5000.74 # float
angajat = True # boolean
# print(nume, " este nascut in anul " + an_nastere + " si este angajat cu un salariu de " + salariu + " lei.")
print(f"{nume} este nascut in anul {an_nastere} si este angajat cu un salariu de {salariu} lei.")

# Assert
assert an_nastere == 1963
assert angajat == True, f"Error, valoarea obtinuta nu este corecta. Expected: True, actual: {angajat}"


# Conversie dintr-un sir de caractere sau string intr-o variabila de tip int care contine valoarea nu mesajul
str_num = "100"
int_num = int(str_num)
# Declaram x ca fiind o variabila de tip in cu valoarea 5
x = 5
# Convertim x intr-un string
x = str(x)
# sau putem sa facem x = "5" daca dorim sa atribuim o valoarea noua fata de cea care era initial

print(type(x)) # <class 'str'>
print(type(str_num)) # <class 'str'>
print(type(int_num)) # <class 'int'>
print(type(is_true)) # <class 'bool'>

# Tranformarea unei variabile string in Boolean, daca variabila contine o valoare, atunci e 1
str = "Hello"
bool_str = bool(str)

print(bool_str) # True

# Tranformarea unei variabile string in Boolean, daca variabila NU contine o valoare, atunci e 0
str = ""
bool_str = bool(str)

print(bool_str) # False

num = int(input("Introdu un numar intreg: "))

print(type(num))  # <class 'int'>

num2 = float(input("Introdu un numar flotant: "))

print(type(num2)) # <class 'float'>

word = input("Introdu un cuvant: ")

print(type(word)) # <class 'str'>

yes_no = input("Introdu da sau nu: ")

if yes_no == "da":
    result = True
else:
    result = False

print(type(result)) # <class 'bool'>



