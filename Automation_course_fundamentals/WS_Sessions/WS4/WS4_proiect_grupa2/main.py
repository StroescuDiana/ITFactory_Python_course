from WS_Sessions.WS4.WS4_proiect_grupa2.Grupa2_exercitiu import Produs, Gestiune


gestiune = Gestiune()

cartofi = Produs(123, "cartofi", 1, 5)
gestiune.adauga_produs(cartofi)

banane = Produs(456, "banane", 2, 8)
gestiune.adauga_produs(banane)

cirese = Produs(789, "cirese", 10, 0)
gestiune.adauga_produs(cirese)

gestiune.cautare_produs(789)
print()
gestiune.cautare_produs(123)
print()
gestiune.cautare_produs(456)
print("---------------------------------------------")

print(f"In stoc se afla {gestiune.produse()} produse.")
print("---------------------------------------------")

gestiune.actualizeaza_cantitate(123, 55)
gestiune.afiseaza_stoc()


#ELIMINAM PRODUS
# gestiune.elimina_produs(123)
# gestiune.elimina_produs(123)

