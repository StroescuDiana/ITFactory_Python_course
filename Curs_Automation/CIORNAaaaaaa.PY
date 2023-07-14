def tuples_imutability_exception():
    # Creating a tuple with a mutable object (list)
    my_tuple = ([1, 2, 3], 'Hello', [4, 5, 6])

    # Modifying the list within the tuple
    my_tuple[0].append(4)
    my_tuple[0][1] = 10

    # Modifying the list outside the tuple
    nested_list = my_tuple[0]
    nested_list.append(5)

    print(my_tuple)  # Output: ([1, 10, 3, 4, 5], 'Hello', [4, 5, 6])


# tuples_imutability_exception()

'''
my_list = "This is an example sentence"
my_list = my_list.lower()
separated_words_list = my_list.split()


# Sort the list in reverse alphabetical order
separated_words_list.sort(reverse=True)
print(separated_words_list)


# Reverse the order of the list
separated_words_list.reverse()
print(separated_words_list)


def even_number(input_string):

    split_input = input_str.split() # separ stringurile la fiecare spatiu

    input_list = [] # creez o lista in care se vor introduce integerii transformati din string
    for num in split_input:
        input_list.append(int(num))


    even_numbers = []
    for i in input_list:
        if i % 2 == 0 :
            even_numbers.append(i)
        else:
            continue

    return even_numbers


input_str = input("Scrie cateva numere: ")
result2 = even_number(input_str)
print(result2)



my_dict = {'name': 'John'}
print(my_dict['name'])
print(my_dict.values())

dict2 = {'age': 20, 'city': 'Oradea'}
my_dict.update(dict2)

print(my_dict)
print(my_dict.keys())
print(my_dict.values())

if 'country' in my_dict:
    print("Country exists in my_dict.")
else:
    print("Error. Country does not exist.")

my_dict.pop('age')
print(my_dict)


my_set = set()
my_set.update([1, 2, 3])
print(len(my_set))

other_set = {2, 3, 4, 5}
print(my_set | other_set)
print(my_set.intersection(other_set))
my_set.remove(2)
if 3 in my_set:
    print("3 se afla in set")

difference_set = my_set.difference(other_set)
print(difference_set)

my_set.clear()
print(my_set) # Output: set()


fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume complet": "Nicolae Dica",
            "Varsta": 45,
            "Numar Tricou": 10
        },
        "Banel": {
            "Nume complet": "Banel Nicolita",
            "Varsta": 47,
            "Numar Tricou": 3
        },
        "Dukadam": {
            "Nume complet": "Helmut Dukadam",
            "Varsta": 65,
            "Numar Tricou": 7
        }
    },
    "Real Madrid": {
        "Ronaldo": {
            "Nume complet": "Cristiano Ronaldo",
            "Varsta": 36,
            "Numar Tricou": 7
        },
        "Benzema": {
            "Nume complet": "Karim Benzema",
            "Varsta": 33,
            "Numar Tricou": 9
        }
    },
    "Manchester United": {
        "Rashford": {
            "Nume complet": "Marcus Rashford",
            "Varsta": 23,
            "Numar Tricou": 10
        },
        "Fernandes": {
            "Nume complet": "Bruno Fernandes",
            "Varsta": 26,
            "Numar Tricou": 18
        }
    }
}

fernandes_player = fotbalisti_pe_echipe["Manchester United"]["Fernandes"].items()
formatted_player = [f"{key}: {value}" for key, value in fernandes_player]



# for i, detail in enumerate(formatted_player):
#     #enumerate(formatted_player): The enumerate() function takes an iterable (formatted_player in this case) and returns an iterator that produces pairs of the form (index, value).
#         #It assigns an index to each element of the iterable, starting from 0. In this case, it pairs the index(i) with the corresponding detail from the formatted_player list.
#     #i, detail: This is known as tuple unpacking. It assigns the index to the variable i and the value (detail) to the variable detail for each pair produced by
#     if i < len(formatted_player) - 1:
#         print(detail, end=", ")
#     else:
#         print(detail)

# for key, value in fotbalisti_pe_echipe["Manchester United"]["Fernandes"].items():
#     print(f"{key}: {value}")




print(fotbalisti_pe_echipe["Real Madrid"])
ronaldo_player = fotbalisti_pe_echipe["Real Madrid"]["Ronaldo"].items()
formatted_ronaldo = [f"{key2}: {value2}" for key2, value2 in ronaldo_player]


benzema_player = fotbalisti_pe_echipe["Real Madrid"]["Benzema"].items()
formatted_benzema = [f"{key2}: {value2}" for key2, value2 in benzema_player]


formatted_players = formatted_benzema + formatted_ronaldo
print(formatted_players)

for x, caracteristici in enumerate(formatted_players):
    if "Nume complet: Cristiano Ronaldo" in caracteristici:
        print()
    print(caracteristici)

class Car:
    wheels = 4 #class variable!!

my_car = Car()
#print(my_car.wheels)

other_car = Car()
#print(other_car.wheels)

my_car.wheels = 6
print("Modificat", my_car.wheels)
print(other_car.wheels)

class Exemplu:
    variabila_statica = 0

    def __init__(self):
        Exemplu.variabila_statica += 1

# Creăm două instanțe ale clasei Exemplu
instanta1 = Exemplu()
instanta2 = Exemplu()

# Afisăm valoarea variabilei statice pentru ambele instanțe
print(instanta1.variabila_statica)  # Output: 2
print(instanta2.variabila_statica)  # Output: 2

# Modificăm valoarea variabilei statice intr-una dintre instanțe
instanta1.variabila_statica = 5

# Afisăm din nou valoarea variabilei statice pentru ambele instanțe
print(instanta1.variabila_statica)  # Output: 5
print(instanta2.variabila_statica)  # Output: 2
'''

class ContBancar:
    numar_conturi = 0

    def __init__(self, numar_de_cont, sold):
        ContBancar.numar_conturi += 1
        self.numar_de_cont = numar_de_cont
        self.sold = sold

    @staticmethod
    def afisare_numar_conturi():
        print(ContBancar.numar_conturi)

    def get_sold(self):
        return self.sold

    def set_new_sold(self, amount):
        self.sold += amount
        return self.sold

    def retragere(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            return self.sold



stroescu_acc = ContBancar(12345, 500)
# print(f"Soldul curent este de {stroescu_acc.get_sold()} lei.")
print(f"Suma adaugata este de 112 lei. Noul sold este de: {stroescu_acc.set_new_sold(112)} lei.")
print(f"Soldul curent este de {stroescu_acc.get_sold()} lei.")

print(stroescu_acc.retragere(300))



'''
if __name__ == '__main__':
    even_number(input_str)

'''
