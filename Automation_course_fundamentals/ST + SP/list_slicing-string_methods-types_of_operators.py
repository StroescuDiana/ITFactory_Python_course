'''
This document contains exercises with:
    -list slicing;
    -string methods;
    -palindrome word
    -operatori >aritmetici
               >de atribuire
               >de comparare
               >logici
'''

def list_slicing():
    # Definim o listă
    my_list = [1, 2, 3, 4, 5]

    # Slicing - obține elementele de la indexul 1 (inclusiv) până la indexul 3 (neinclusiv)
    sliced_list = my_list[1:3]
    print(sliced_list)  # Output: [2, 3]

    # Slicing - obține elementele de la începutul listei până la indexul 2 (neinclusiv)
    sliced_list = my_list[:2]
    print(sliced_list)  # Output: [1, 2]

    # Slicing - obține elementele de la indexul 2 (inclusiv) până la sfârșitul listei
    sliced_list = my_list[2:]
    print(sliced_list)  # Output: [3, 4, 5]

    # Slicing - obține elementele de la indexul -3 (inclusiv) până la indexul -1 (neinclusiv),
    # adică ultimele două elemente ale listei
    sliced_list = my_list[-3:-1]
    print(sliced_list)  # Output: [3, 4]

    # Slicing - obține fiecare al doilea element din lista
    sliced_list = my_list[::2]
    print(sliced_list)  # Output: [1, 3, 5]

def textNumbers():
    text_numbers = "0123456789"

    print(text_numbers[3]) # valoarea de la indexul 3, incepe de la 0

    print(text_numbers[1:6]) # de la indexul 0 al stringului pana la 5 sunt 6 pozitii

    print(text_numbers[5::]) # incepand cu pozitia 5 afiseaza tot sirul pana la final: start

    print(text_numbers[:5]) # toate valorile pana la pozitia 5, dar nu inclusiv 5: stop

    print(text_numbers[::2]) # din 2 in 2 incepand cu pozitia 0, numere pare

    print(text_numbers[1::2]) # din 2 in 2 numere impare

    print(text_numbers[::-1]) # ordine inversa

    print(text_numbers[-4:]) # ultimele 4 caractere

    print(text_numbers[-4::-1]) # incepand cu a patra pozitie din ordine inversa afiseaza tot pana la ultima care e 0

def string_methods():
    # Definim un șir de caractere
    my_string = "Astăzi este o zi frumoasă de vară 123."

    # Folosim replace() pentru a înlocui un subșir în interiorul șirului
    new_string = my_string.replace("frumoasă", "însorită")
    print(new_string)  # Output: "Astăzi este o zi însorită de vară 123."

    # Folosim upper() pentru a converti toate caracterele din șir în majuscule
    print(my_string.upper())  # Output: "ASTĂZI ESTE O ZI FRUMOASĂ DE VARĂ 123."

    # Folosim lower() pentru a converti toate caracterele din șir în minuscule
    print(my_string.lower())  # Output: "astăzi este o zi frumoasă de vară 123."

    # Folosim split() pentru a împărți șirul într-o listă de cuvinte
    words = my_string.split()
    print(words)  # Output: ["Astăzi", "este", "o", "zi", "frumoasă", "de", "vară", "123."]

    # Folosim index() pentru a găsi indexul unui subșir în interiorul șirului
    index = my_string.index("zi")
    print(index)  # Output: 4

    # Folosim islower() pentru a verifica dacă șirul este format doar din caractere mici
    print(my_string.islower())  # Output: False

    # Folosim capitalize() pentru a face majusculă prima literă din șir
    print(my_string.capitalize())  # Output: "Astăzi este o zi frumoasă de vară 123."

    # Folosim isdecimal() pentru a verifica dacă șirul este un număr zecimal
    print(my_string.isdecimal())  # Output: False

    # Folosim isdigit() pentru a verifica dacă șirul este un număr sau conține doar cifre
    print(my_string.isdigit())  # Output: False

    # Folosim isnumeric() pentru a verifica dacă șirul este un șir numeric
    print(my_string.isnumeric())  # Output: False

    # Folosim count() pentru a număra numărul de apariții ale unui subșir în interiorul șirului
    count = my_string.count("a")
    print(count)  # Output: 5

    my_string = "Acesta este un exemplu de șir pentru a număra cuvintele."
    words = my_string.split()
    num_words = len(words)
    print(num_words)  # Output: 8

# Acest program determină dacă un șir dat este palindrom sau nu

def este_palindrom(sir):
    """
    Un palindrom este un șir de caractere care poate fi citit la fel de bine de la stânga la dreapta și de la dreapta la stânga.
    Adică, șirul rămâne același atunci când este inversat.
    """
    sir = sir.lower() # Convertim totul la litere mici pentru a evita erorile de capitalizare
    sir = sir.replace(" ", "") # Eliminăm spațiile pentru a nu le lua în considerare în verificarea palindromului
    invers = sir[::-1] # Folosim segmentarea pentru a inversa șirul
    print(sir)
    print(invers)
    return sir == invers # Verificăm dacă șirul invers este egal cu șirul original

def operatori_aritmetici():
    # Definim două variabile numerice
    a = 10
    b = 3

    # Adunarea a două numere
    suma = a + b
    print("Suma:", suma)

    # Scăderea dintre două numere
    diferenta = a - b
    print("Diferenta:", diferenta)

    # Înmulțirea a două numere
    produs = a * b
    print("Produs:", produs)

    # Împărțirea unui număr la altul (împărțire exactă)
    cat = a // b
    print("Catul:", cat)

    # Împărțirea unui număr la altul (împărțire cu zecimală)
    cat_zecimal = a / b
    print("Catul zecimal:", cat_zecimal)

    # Restul împărțirii a două numere
    rest = a % b
    print("Restul:", rest)

    # Ridicarea unui număr la o putere
    putere = a ** b
    print("Puterea:", putere)

    # Definim un număr
    numar = 10

    # Calculăm câte bucăți de 2 pot fi împărțite din numărul dat
    bucati_de_2 = numar // 2

    # Afișăm rezultatul
    print("Numărul de bucăți de 2 care se pot împărți din", numar, "este", bucati_de_2)

def operatori_de_atribuire():
    # Definim o variabilă numerică
    x = 10

    # Operatorul de atribuire simplă
    y = x
    print("y =", y)

    # Operatorul de atribuire cu adunare
    y += 5
    print("y =", y)

    # Operatorul de atribuire cu scădere
    y -= 3
    print("y =", y)

    # Operatorul de atribuire cu înmulțire
    y *= 2
    print("y =", y)

    # Operatorul de atribuire cu împărțire
    y /= 4
    print("y =", y)

    y = 14

    # Operatorul de atribuire cu rest
    y %= 3
    print("y =", y)

    y = 11
    # Operatorul de atribuire cu împărțire exactă
    y //= 2
    print("y =", y)

    # Operatorul de atribuire cu ridicare la putere
    y **= 3
    print("y =", y)

def operatori_de_comparare():
    # Definim două variabile numerice
    a = 10
    b = 5

    # Operatorul de egalitate
    if a == b:
        print("a este egal cu b")
    else:
        print("a nu este egal cu b")

    # Operatorul de inegalitate
    if a != b:
        print("a este diferit de b")
    else:
        print("a este egal cu b")

    # Operatorul de mai mare decât
    if a > b:
        print("a este mai mare decât b")
    else:
        print("a nu este mai mare decât b")

    # Operatorul de mai mic decât
    if a < b:
        print("a este mai mic decât b")
    else:
        print("a nu este mai mic decât b")

    # Operatorul de mai mare sau egal
    if a >= b:
        print("a este mai mare sau egal decât b")
    else:
        print("a nu este mai mare sau egal decât b")

    # Operatorul de mai mic sau egal
    if a <= b:
        print("a este mai mic sau egal decât b")
    else:
        print("a nu este mai mic sau egal decât b")

def operatori_logici():
    # Define the variables
    angajat = True
    salariu = 2000

    # Use logical operators to evaluate conditions
    if angajat and salariu > 1500:
        print("Angajatul are un salariu mare.")
    else:
        print("Angajatul nu are un salariu mare.")

    if not angajat or salariu >= 3000:
        print("Angajatul nu este in prezent angajat sau are un salariu mare.")
    else:
        print("Angajatul este in prezent angajat si nu are un salariu mare.")\

def if_else():
    varsta = 25
    venit = 50000

    if varsta < 18:
        print("Sunteți prea tânăr pentru a lucra.")
    elif varsta >= 18 and varsta <= 65:
        if venit >= 50000:
            print("Sunteți eligibil pentru un împrumut.")
        else:
            print("Nu sunteți eligibil pentru un împrumut.")
    else:
        print("Sunteți prea bătrân pentru a lucra.")

# Testăm funcția noastră
test_1 = "A man a plan a canal Panama"
test_2 = "Not a palindrome"
print(este_palindrom(test_1)) # Așteptăm True
print(este_palindrom(test_2)) # Așteptăm False

# operatori_aritmetici()
# operatori_de_atribuire()

text = "string"
