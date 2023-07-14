#Ex_7 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''
def vocala_consoana(str_input):

    if str_input in ("a", "e", "i", "o", "u"):
        print(f"Litera {str_input} este o vocala.")
    elif str_input in ("a", "e", "i", "o", "u"):
        print(f"Litera {str_input} este o vocala.")
    else:
        print(f"Litera {str_input} este o consoana.")


str_input = input("Scrie o litera din alfabet: ")
vocala_consoana(str_input)


def calculare_pret_discount(client_age):
    x = 0 # reducerea

    input_anotimp = input("In ce luna doriti sa calatoriti?")
    primavara = ("martie", "aprilie", "mai")
    vara = ("iunie", "iulie", "august")
    toamna = ("septembrie", "octombrie", "noiembrie")
    iarna = ("decembrie", "ianuarie", "februarie")

    child_option = input("Calatoriti impreuna cu un copil?")
    taxa_lux = input("Doriti sa calatoriti la clasa I?")

    if client_age > 65 and input_anotimp.lower() in iarna:
        x = x + 25
    else:
        pass

    if client_age < 65 and child_option == "yes":
        x = x + 10
        if input_anotimp.lower() in iarna:
            x = x + 10
    else:
        pass

    if taxa_lux == "yes":
        x = x - 3
    else:
        x = x - 1

    print(f"Reducerea finala este de {x}%. Pretul final este de {1200 * x / 100} lei.")


client_age = int(input("Introduceti varsta dumneavoastra: "))
calculare_pret_discount(client_age)
'''

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




