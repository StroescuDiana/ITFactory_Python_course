from abc import abstractmethod, ABC


class Gradinita(ABC): #It cannot be instantiated, and serves as a blueprint for subclasses.
    @abstractmethod
    def joaca(self):
        raise NotImplementedError  # am instruit sistemul sa returneze o eroare specifica daca metoda nu este implementata

    def somn(self):
        pass

    @abstractmethod
    def activitati(self):
        pass


class Gradinita_privata(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("copiii alearga")

    def activitati(self):
        print("Copiii coloreaza")


class Gradinita_publica(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("copiii sar coarda")

    def activitati(self):
        print("Copiii canta")

