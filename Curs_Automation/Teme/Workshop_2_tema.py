'''
#8. Verificati diferenta intre doua seturi cu functia difference()
first_set = {1, 2, 3, 4}
second_set = {4, 5, 6, 7}
print(first_set.difference(second_set))

#9. Stergeti toate elementele dintr-un set folosind functia clear()
second_set.clear()
print(second_set)

---------------------------- DICTIONARY EXERCISES ----------------------------

#1. Declarati un dictionar
my_dict = {"fruit": "banana", "color": "yellow", "bought": "2 days ago"}

#2. Declarati un dictionar gol
empty_dict = dict()

#3. Adaugati un element nou in dictionar folosind functia update() si respectiv pe baza de cheie
basic_dict = {"name": "Real", "surname": "Madrid"}

my_dict.update(basic_dict)
print(my_dict)

# alta metoda de a adauga element in dictionar
basic_dict.setdefault("age", 12)
print(basic_dict)

#4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
print(my_dict.get("bought"))

#5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem(). Observati rezultatele
my_dict.pop("bought") # sterge valoarea si o returneaza de la cheia indicata
print(my_dict)

my_dict.popitem() # sterge ultima cheie-valoare ALEATORIE
print(my_dict)

#6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile din dictionar
new_dict = {'kzqke': 93, 'lyhmo': 45, 'hbuqu': 79}
for key in new_dict.key():
    print(key)

for val in new_dict.values():
    print(val)

print([item for item in new_dict.items()]) # ---- list comprehension ----
'''

# Aveti urmatorul dictionar (dictionar imbricat / nested dictionary / embedded dictionary):
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
    }
}

# print(fotbalisti_pe_echipe["Barcelona"]["Dica"]["Numar Tricou"]) #metoda 1
# print(fotbalisti_pe_echipe.get("Barcelona").get("Dica").get("Numar Tricou")) #metoda 2

# metoda 3
# barcelona = fotbalisti_pe_echipe.get("Barcelona")
# dica = barcelona.get("Dica")
# numar_tricou_dica = dica.get("Numar Tricou")
# print(numar_tricou_dica)
# print(type(numar_tricou_dica))


# fotbalisti_pe_echipe["Barcelona"].pop("Banel")

# for jucator, detalii in fotbalisti_pe_echipe["Barcelona"].items():
#     print("Detalii jucator - Nume complet:", detalii["Nume complet"], end=", ")
#     print("Detalii jucator - Varsta:", detalii["Varsta"], end=", ")
#     print("Detalii jucator - Numar Tricou:", detalii["Numar Tricou"])

# The end=", " argument in the print() statements ensures
#   that the output is printed on the same line, separated by commas and a space.


cv_dict = {
    "Informatii personale": {
        "Nume": "Stroescu Diana",
        "Adresa": "Strada Kogalniceanu",
        "Numar de telefon": 1234567890,
        "E-mail": "fake_account@yahoo.com"
    },

    "Educatie": {
        "Studii superioare": ("Universitatea X", 2018),
        "Liceu": ("Liceul Y", "Filologie-bilingv", 2014)
    },

    "Experienta profesionala": {
        "Producer": {
            "Companie": "HaHa Production",
            "Poziție": "Producer",
            "Perioadă": "Iulie 2019 - Prezent"
        },
        "Tester": {
            "Companie": "Microsoft",
            "Poziție": "automation tester",
            "Perioadă": "noiembrie 2020 - Prezent"
        }
    },
    "Abilitati lingvistice": ["romana", "engleza", "germana"],
    "Proiecte relevante": [
        ("proiect_1", 2016),
        ("proiect_2", 2017)
    ],
    "Hobiuri": ["muzica", "calatorii", "sport", "F1"]
}

#print(cv_dict)
#print(cv_dict.get("Educatie").get("Liceu")[0])
cv_dict["Experienta profesionala"]["Tester"]["Perioadă"] = "noiembrie 2017 - iulie 2019"

#print(cv_dict["Experienta profesionala"]["Tester"]["Perioadă"])

cv_dict["Abilitati lingvistice"].append("franceza")
#print(cv_dict["Abilitati lingvistice"])

cv_dict["Proiecte relevante"][1] = ("proiect_2", 2018)
print(cv_dict["Proiecte relevante"][1])