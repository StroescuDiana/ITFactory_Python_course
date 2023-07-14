"""
ALT +  ENTER = importeaza
"""

from mini_proiect.Mostenire import GradinitaPublica


class GradinitaPublica25(GradinitaPublica):

    def __init__(self, nume_profesor: str, nr_copii: int, nume_copii: list):
        self.nume_profesor = nume_profesor
        self._nr_copii = nr_copii
        self.__nume_copii = nume_copii


    def activitate_practica(self):
        print("Copiii se joaca in curte pe balansoar.")

    def medie_buline_rosii(self):
        nr_copii = int(input("Introdu nr copii: "))

        total_buline_rosii = 0
        for _ in range(nr_copii):
            buline_rosii = int(input("Buline rosii: "))
            total_buline_rosii += buline_rosii

        medie_buline_rosii = total_buline_rosii / nr_copii

        if medie_buline_rosii > 5:
            print("Sunt foarte neastamparati.")
        else:
            print("Copii sunt buni.")

    @property  # ------------> alegem variabila de instanta asupra careia se fac getter / setter / del
    def nume_copii(self):
       pass

    @nume_copii.getter
    def nume_copii(self):
        return self.__nume_copii

    @nume_copii.setter
    def nume_copii(self, nume: list):
        self.__nume_copii = nume

    @nume_copii.deleter
    def nume_copii(self):
        del self.__nume_copii  # ---> DEL sterge complet



