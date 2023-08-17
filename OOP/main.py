from GradinitaPublica25 import GradinitaPublica25
from Mostenire import GradinitaPublica, GradinitaPrivata

gradinita_publica = GradinitaPublica()

gradinita_publica.ora_de_somn()
gradinita_publica.activitate_practica()
print()

gradinita_privata = GradinitaPrivata()
gradinita_privata.activitate_practica()
gradinita_privata.ora_de_somn()
print()

gradinita25 = GradinitaPublica25("pop mihai", 56, ["copil1", "copil2", "copil3", "copil4"])
print(gradinita25.nume_profesor)
print(gradinita25.nume_copii)  # ----> cand apelam getter nu punem paranteze

gradinita25.nume_copii = ["copil5", "copil6", "copil7", "copil8"]  # ----> schimba valoarea variabilei private nume_copii
print(f"Variabila privata __nume_copii a fost schimbata cu: {gradinita25.nume_copii}")

#del gradinita25.nume_copii  ----> stergem cu del variabila privata __nume_copii






