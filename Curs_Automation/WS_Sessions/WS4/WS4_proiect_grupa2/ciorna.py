class Produs:
    def __init__(self, cod: int, nume: str, pret: int, cantitate: int):
        self.cod = cod
        self.nume = nume
        self.pret = pret
        self.cantitate = cantitate

class Gestiune:
    def __init__(self):
        self.__produse_disponibile = {}

    def adauga_produs(self, produs: Produs):
        if produs.cod not in self.__produse_disponibile:
            #declar o variabila noua de tip DICTIONARY-
            #   De ce DICTIONARY? = pt ca valorile sunt mai usor de accesat si codul e mai structurat
            #-care sa contina datele produsului ce urmeaza a fi adaugat(in sistem) in perechi cheie - valoarea produsului
            produs_adaugat = {
                "cod": produs.cod,
                "nume": produs.nume,
                "pret": produs.pret,
                "cantitate": produs.cantitate,
            }
            #Explanation(line 49):
            # If you want to keep track of multiple products, it's important to use a dictionary
            # to store each product as a separate key-value pair, where the key is the product code
            # and the value is a nested dictionary containing the product details.
            self.__produse_disponibile[produs.cod] = produs_adaugat
        else:
            print(f"Un produs cu același cod {produs.cod} există deja.")

    def elimina_produs(self, cod):
        #Check if the given cod parameter exists as a key in the self.produse_disponibile dictionary
        if cod not in self.__produse_disponibile:
            print(f"Produsul, avand codul {cod}, nu se afla in sistem.")
        else:
            #The entire nested dictionary associated with the key cod(parameter) will be deleted,
            # including the "cod", "nume", "pret", "cantitate" key-value pairs.
            del self.__produse_disponibile[cod]
            print(f"Produsul, avand codul {cod}, a fost eliminat.")

    def actualizeaza_cantitate(self, cod: int, cantitate: int):
        if cod in self.__produse_disponibile:
            self.__produse_disponibile.get(cod)["cantitate"] = cantitate


    def afiseaza_stoc(self):
        for cod, produs in self.__produse_disponibile.items():
            if produs["cantitate"] > 0:
                print(f"Cod: {cod}, Nume: {produs['nume']}, Pret: {produs['pret']}, Cantitate: {produs['cantitate']}")
            else:
                continue

    def cautare_produs(self, cod):
        if cod in self.produse_disponibile:
            detalii_produs = self.__produse_disponibile.get(cod)
            if detalii_produs["cantitate"] > 0:
                print("Detalii produs:")
                print(f"Cod: {detalii_produs['cod']}, Nume: {detalii_produs['nume']}, Pret: {detalii_produs['pret']}, Cantitate: {detalii_produs['cantitate']}")

            else:
                print(f"Produsul, avand codul {cod}, nu se afla in stoc.")


    @property
    def produse_disponibile(self):
        pass

    @produse_disponibile.getter
    def produse_disponibile(self):
        return self.__produse_disponibile

    def produse(self):
        produse_in_stoc = []  #stocheaza produsele in stoc
        for cod, produs in self.__produse_disponibile.items():
            if produs["cantitate"] > 0:
                produse_in_stoc.append(cod)

            else:
                continue
        return len(produse_in_stoc)


