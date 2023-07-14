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
            produs_adaugat = {
                "cod": produs.cod,
                "nume": produs.nume,
                "pret": produs.pret,
                "cantitate": produs.cantitate
            }
            self.__produse_disponibile[produs.cod] = produs_adaugat
        else:
            print(f"Un produs cu același cod {produs.cod} exista deja.")

    def elimina_produs(self, cod):
        if cod not in self.__produse_disponibile:
            print(f"Produsul, avand codul {cod}, nu se afla in sistem.")
        else:
            del self.__produse_disponibile[cod]
            print(f"Produsul, avand codul {cod}, a fost eliminat.")

    def actualizeaza_cantitate(self, cod: int, cantitate_noua: int):
        if cod in self.__produse_disponibile:
            self.__produse_disponibile.get(cod)["cantitate"] = cantitate_noua

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

    # @property
    # def produse_disponibile(self):
    #     pass

    #daca avem nevoie doar de getter, atunci scriem doar property pt ca by default creeaza un getter
    @property
    def produse_disponibile(self):
        return self.__produse_disponibile

    def produse(self):
        produse_in_stoc = []
        for cod, produs in self.__produse_disponibile.items():
            if produs["cantitate"] > 0:
                produse_in_stoc.append(cod)
            else:
                continue

        return len(produse_in_stoc)