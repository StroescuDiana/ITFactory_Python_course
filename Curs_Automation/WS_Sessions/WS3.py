'''
# variabilele nu se declara cu cifre: 3D NU se poate
# DACA vrem sa ne folosim de atributele unei CLASE, trebuie sa utilizam self.
# De PREFERAT sa nu mai scriu else, pt if ci sa scriu direct rezultatul

#1 Creati o clasa cinema in care sa stocati atributele si metodele de care e nevoie ca sa puteti sa gestiona un sistem de tip cinema (acestea vor fi implementate la alegerea voastra). Clasa nu va avea constructor.

#2 Creati cel putin 5 metode de test si 10 atribute.

#3 Apelati pe rand fiecare dintre metodele create si respectiv printati  pe ecran toate valorile atributelor pentru fiecare obiect. Printarea se va face cu formatare si, pentru o complexitate mai mare, puteti sa puneti toate obiectele instantiate intr-o lista pe care sa o parcurgeti cu un for (si astfel sa faceti printarea pentru toate elementele concomitent). Repetati actiunea cu while si respectiv cu foreach. Rulati codul.

#4 Modificati clasa prin adaugarea unui constructor care sa primeasca doi parametri care sa populeze, la alegere, doua dintre atributele definite in clasa. Rulati codul. Ce observati?

#5 Faceti modificarile necesare astfel incat sistemul sa nu mai returneze eroare.

#6 Modificati constructorul astfel incat sa controlati valorile care sunt salvate in fiecare atribut. Spre exemplu: daca se incearca salvarea numarului de locuri pentru cinema cu un numar mai mare de 500 sa se printeze pe ecran  o eroare.

#7 Rulati codul din nou si introduceti o valoare care sa nu respecte conditia definita in constructor (ex: un numar de locuri mai mare decat 500). Ce observati?
'''



class Cinema:
    # atribute de clasa
    are_3D = True
    ora_deschidere = 11_00
    ora_inchidere = 24_00

    # metoda CONSTRUCTOR
    def __init__(self, nume, locatie):
        # variabile de instanta
        self.nume = nume
        self.locatie = locatie
        self.sali = {
            "Sala 1": 250,
            "Sala 2": 350,
            "Sala 3": 450
        }
        self.preturi = {
            "Avatar": 35,
            "Iron Man": 30,
            "Gardienii Galaxiei": 40
        }
        self.filme = ["Avatar", "Iron Man", "Gardienii Galaxiei"]
        self.discount_aplicat = False
        # END of variabile de instanta

    def afiseaza_detalii(self):
        return f"{self.nume}, localizat in {self.locatie}."

    def afiseaza_filme_disponibile(self):
        return f"In acest moment se ruleaza pe marile ecrane: {', '.join(self.filme)}."

    def afiseaza_preturi(self):
        for film, pret in self.preturi.items():
            print(f"Pretul pentru filmul {film} este {pret} lei.")

    def verifica_3D(self):
        if self.are_3D:
            return "Cinematograful suporta functia 3D."

        return "Cinematograful nu suporta functia 3D"

    def verifica_program(self, ora):
        # 11:00 <= 13:00 <= 24:00
        if self.ora_deschidere <= ora and ora <= self.ora_inchidere:
            return f"Cinematograful {self.nume} este deschis."

        return f"Cinematograful este inchis."

    def selecteaza_discount(self, tip):
        if tip == "elev" or tip == "student":
            discount = 0.2
        elif tip == "pensionar":
            discount = 0.3
        else:
            discount = 0

        return discount

    def aplica_discount(self, pret_vechi, discount):
        return pret_vechi - pret_vechi * discount

    def selecteaza_filmul(self):
        return self.filme



# instantierea unui obiect/ crearea unei instante a clasei !!!
cinema_oradea = Cinema("Cinema City", "Oradea")
# cinema_iasi = Cinema("Cinema City", "Iasi")
# cinema_bucuresti = Cinema("Cinema City", "Bucuresti")
# cinema_brasov = Cinema("Cinema City", "Brasov")

print(cinema_oradea.afiseaza_detalii())
print(cinema_oradea.afiseaza_filme_disponibile())
cinema_oradea.afiseaza_preturi()
print(cinema_oradea.verifica_3D())
print(cinema_oradea.verifica_program(13_00))

pret_avatar = 35
discount = cinema_oradea.selecteaza_discount("student")
pret_final = cinema_oradea.aplica_discount(pret_avatar, discount)
print(pret_final)





