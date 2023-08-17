'''#Ex_7 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
def vocala_consoana(str_input):

    if str_input in ("a", "e", "i", "o", "u"):
        print(f"Litera {str_input} este o vocala.")
    elif str_input in ("a", "e", "i", "o", "u"):
        print(f"Litera {str_input} este o vocala.")
    else:
        print(f"Litera {str_input} este o consoana.")


str_input = input("Scrie o litera din alfabet: ")
vocala_consoana(str_input)
'''

'''
Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.

def calculare_pret_discount(client_age):
    x = 0  # reducerea

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





