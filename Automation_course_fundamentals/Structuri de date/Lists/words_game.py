def schimba_ultima_aparitie_cuvantului_mere_cu_pere(string):

    string = string.replace("ă", "a")
    cuvinte = string.split()
    last_index = len(cuvinte)-1 - cuvinte[::-1].index("mere")
    cuvinte[last_index] = "pere"
    text = " ".join(cuvinte)
    print(text)

schimba_ultima_aparitie_cuvantului_mere_cu_pere("mere mere mere mere")

# o metoda ce separa in lista
def schimba_ultima_aparitie_literei_in_sir(string, litera_veche, litera_noua):
    # separa sirul in cuvinte
    cuvinte = list(string)

    # gaseste indexul la care se afla ultimul ă
    last_litera_veche_index = len(cuvinte) - 1 - cuvinte[::-1].index(litera_veche)

    # inlocuieste ultimul a cu a in ultimul cuvant
    cuvinte[last_litera_veche_index] = litera_noua

    # puen cuvintele inapoi in propozitie
    new_string = "".join(cuvinte)

    print(new_string)
    # Astăzi este o zi frumoasî de vară 123

# o metoda ce separa cu split() in cuvinte
def schimba_ultima_aparitie_literei_in_sir_2(string, litera_veche, litera_noua):
    caractere = list(string)

    last_index = len(caractere) - 1 - caractere[::-1].index(litera_veche)

    # schimba caracterul
    caractere[last_index] = litera_noua

    new_string = "".join(caractere)
    print(new_string)


schimba_ultima_aparitie_literei_in_sir_2("Astăzi este o zi frumoasă de vară 123.", "ă", "a")

schimba_ultima_aparitie_literei_in_sir("Astăzi este o zi frumoasă de vară 123.","ă", "a")