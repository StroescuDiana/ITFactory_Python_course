def list_slicing():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    '''sliced_list = my_list[1::2]
    print(sliced_list)
    '''
    #print(my_list[1::2])
    print(len(my_list))
#list_slicing()

'''
my_string = "astăzi este o zi frumoasă de vară 123."
new_string = my_string.split()
print(len(new_string))

last_index = len(new_string) - 1

print(new_string[last_index])

print(new_string)
print(new_string.index("123."))
#print(my_string.count("a"))
'''

def schimba_ultima_aparitie_literei_in_sir(string, litera_veche, litera_noua):
    # separa sirul in caractere
    caractere = list(string)
    print(caractere)
    print(len(caractere))

    # gaseste indexul la care se afla ultimul ă
    last_litera_veche_index = len(caractere) - 1 - caractere[::-1].index(litera_veche)
    print("indexul ultimului ă: ", last_litera_veche_index)

    # inlocuieste ultimul ă cu a in ultimul cuvant
    caractere[last_litera_veche_index] = litera_noua

    # pun caracterele inapoi in propozitie
    new_string = "".join(caractere)
    print(new_string)


schimba_ultima_aparitie_literei_in_sir("Astăzi este o zi frumoasă de vară 123", "ă", "a")