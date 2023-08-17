from abc import ABC, abstractmethod

class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Aceasta metoda nu este implementata.")








