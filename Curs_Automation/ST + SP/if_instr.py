"""
Clauza if-else este o structură de control în Python care permite executarea de cod diferit în funcție de o condiție
if condition:
    # Execută codul dacă condiția este adevărată
    statement1
    statement2
    ...
else:
    # Execută codul dacă condiția este falsă
    statement3
    statement4
    ...
"""

# Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = int(input("Introduceti un numar: "))

if x >= 0 and isinstance(x, int):
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")

#Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = float(input("Introduceti un numar: "))

if x > 0:
    print(f"{x} este un numar pozitiv.")
elif x < 0:
    print(f"{x} este un numar negativ.")
else:
    print(f"{x} este un numar neutru (zero).")

# Ex_3 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = float(input("Introduceti un numar: "))

if -2 <= x <= 13:
    print(f"{x} se afla intre -2 si 13.")
else:
    print(f"{x} nu se afla intre -2 si 13.")

# Ex_4 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)

x = float(input("Introduceti un numar: "))

if not (5 < x < 27):
    print(f"{x} nu se afla intre 5 si 27 (excluzand capetele de interval).")
else:
    print(f"{x} se afla intre 5 si 27 (excluzand capetele de interval).")

#Ex_5 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

x = int(input("Introduceti valoarea pentru x: "))
y = int(input("Introduceti valoarea pentru y: "))

if x == y:
    print("x și y sunt egale.")
else:
    if x > y:
        print("x este mai mare decât y.")
    else:
        print("y este mai mare decât x.")

#Ex_6 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi,
# afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale)
# sau oarecare (nicio latura nu e egala).

x = int(input("Introduceti lungimea primei laturi: "))
y = int(input("Introduceti lungimea celei de-a doua laturi: "))
z = int(input("Introduceti lungimea celei de-a treia laturi: "))

if x == y == z:
    print("Triunghiul este echilateral.")
elif x == y or y == z or z == x:
    print("Triunghiul este isoscel.")
else:
    print("Triunghiul este oarecare.")

#Ex_7 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = input("Introduceți o literă: ")

# Convertim litera introdusă la lowercase pentru a simplifica verificările
litera = litera.lower()

if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print("Litera introdusă este o vocală.")
else:
    print("Litera introdusă nu este o vocală.")

"""
Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% 
dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
"""
def calculare_pret_discount():
    varsta_client = int(input("Introduceți vârsta clientului: "))
    nr_copii = int(input("Introduceți numărul de copii călătorind cu clientul: "))
    clasa_calatorie = input("Introduceți clasa de călătorie (I sau II): ")
    sezon_iarna = input("Călătoriți în timpul iernii? (da sau nu): ")

    pret_bilet = 100  # prețul inițial al biletului

    # Verificăm dacă clientul are peste 65 de ani
    if varsta_client >= 65:
        pret_bilet -= pret_bilet * 0.15  # se aplică reducerea de 15% pentru seniori

        # Verificăm dacă călătorește în timpul iernii și se aplică o reducere suplimentară de 10%
        if sezon_iarna.lower() == 'da':
            pret_bilet -= pret_bilet * 0.1

    # Verificăm dacă clientul nu are peste 65 de ani și călătorește cu cel puțin un copil
    elif nr_copii > 0:
        pret_bilet -= pret_bilet * 0.1  # se aplică reducerea de 10% pentru călătorii cu copii

        # Verificăm dacă călătorește în timpul iernii și se aplică o reducere suplimentară de 10%
        if sezon_iarna.lower() == 'da':
            pret_bilet -= pret_bilet * 0.1

    # Verificăm clasa de călătorie pentru aplicarea taxelor
    if clasa_calatorie.lower() == 'i':
        pret_bilet += pret_bilet * 0.03  # se adaugă taxa de lux de 3% pentru clasa I
    else:
        pret_bilet += pret_bilet * 0.01  # se adaugă taxa de gestiune de 1% pentru clasa II

    print("Prețul final al biletului este:", pret_bilet)


"""
Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. 
Clienții angro primesc o reducere de două procente la toate comenzile. 
De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul să plătească ramburs la livrare,
oferind o reducere de două procente pentru această metodă de plată. 
Încă o reducere de două procente este acordată pentru comenzile de 50 sau mai multe unități. 
Fiecare coloană reprezintă un anumit tip de ordine.

"""
def calculate_discount(order_type, order_quantity, payment_method):
    discount = 0

    if order_type == 'angro':
        discount += 2  # reducere de 2% pentru clienții angro

    if payment_method == 'ramburs':
        discount += 2  # reducere de 2% pentru plata ramburs

    if order_quantity >= 50:
        discount += 2  # reducere de 2% pentru comenzile de 50 sau mai multe unități

    return discount


# Exemplu de utilizare:
order_type = input("Introduceți tipul comenzii (angro sau amanunt): ")
order_quantity = int(input("Introduceți cantitatea comenzii: "))
payment_method = input("Introduceți metoda de plată (ramburs sau alta): ")

discount = calculate_discount(order_type, order_quantity, payment_method)
print("Discount-ul pentru comanda este:", discount, "%")

"""
Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este numele filmului vostru preferat. 
Daca da, atunci printati pe ecran: “Acesta este filmul meu preferat”. In caz contrar printati pe ecran: 
Din pacate nu este filmul meu preferat”
"""
def favorite_film():
    favorite_film = "Inception"  # Your favorite film's name


    film_name = input("Introduceți numele unui film: ")

    if film_name == favorite_film:
        print("Acesta este filmul meu preferat.")
    else:
        print("Din păcate nu este filmul meu preferat.")

def list_favorite_movies():
    favorite_movies = ["Inception", "The Shawshank Redemption", "Pulp Fiction", "The Dark Knight", "Fight Club"]

    film_name = input("Introduceți numele unui film: ")

    if film_name in favorite_movies:
        print("Acesta este unul dintre filmele mele preferate.")
    else:
        print("Din păcate nu este unul dintre filmele mele preferate.")

"""
Aveti la dispozitie urmatorul database url: jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date este cel corect 
(presupunand ca extrageti url-ul dintr-un sistem extern si nu stiti care este acesta)
"""
def database_url():
    database_url = "jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC"

    # Extrage numele bazei de date din URL
    start_index = database_url.find("//") + 2
    end_index = database_url.find(":", start_index)
    extracted_database_name = database_url[start_index:end_index]

    # Verifică dacă numele bazei de date este cel corect
    correct_database_name = "mysql.db.server"

    if extracted_database_name == correct_database_name:
        print("Numele bazei de date este corect.")
    else:
        print("Numele bazei de date nu este corect.")
