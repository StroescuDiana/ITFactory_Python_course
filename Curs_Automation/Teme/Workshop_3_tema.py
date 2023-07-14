'''
A. Creați o clasă "Student" care să aibă următoarele atribute:

1. Nume (șir de caractere): reprezintă numele complet al studentului.
2. Vârstă (nr. întreg): reprezintă vârsta studentului.
3. Specializare (șir de caractere): reprezintă specializarea de studiu a studentului.
4. Note: stochează notele studentului; setați acest parametru drept parametru cu număr variabil, fiecare număr fiind tratat ca nr. întreg.
5. Medie (nr. zecimal): reprezintă media notelor obținute de student; setați valoarea implicită pe 0(va fi calculată ulterior).

B. Implementați un constructor care să primească ca parametri numele, vârsta, specializarea și notele studentului și să le atribuie corespunzător atributelor clasei; folosiți și definirea tipului de date specific fiecărui parametru.

C. Implementați o metodă "calculeaza_medie()" care să calculeze media studentului pe baza valorilor atributului „note” și să actualizeze atributul "medie" al obiectului.

D. Implementați o metodă "afiseaza_detalii()" care să afișeze pe ecran toate detaliile despre student: nume, vârstă, specializare și medie.

E. Implementați o metodă "este_promovat()" care să verifice dacă media studentului este mai mare sau egală cu 5.0 și să returneze un mesaj corespunzător, indicând dacă studentul este promovat sau nu.

F. Testați clasa "Student" prin crearea a câțiva studenți și apelarea metodelor implementate.
'''


class Student:

    def __init__(self, nume: str, varsta: int, specializare: str, *note: int):
        self.nume = nume
        self.varsta = varsta
        self.specializare = specializare
        self.note = list(note)  # ---> type cast la LIST pentru ca un student poate sa mai primesca ulterior alte note, nu raman aceleasi note
        self.medie = 0

# C: Implementați o metodă "calculeaza_medie()" care să calculeze media studentului pe baza valorilor atributului „note” și
    # să actualizeze atributul "medie" al obiectului.
    def calculeaza_medie(self):
        if not len(self.note) >= 2:
            return f"Studentul trebuie sa aiba cel putin 2 note pentru a avea medie."
        self.medie = sum(self.note) / len(self.note)
        return self.medie

        #nr_note = len(self.note)  # ---> aflu cate note se afla in lista

        # suma_note = 0
        # for nota in self.note:
        #     suma_note += nota
        #
        # self.medie = suma_note / nr_note
        # return self.medie

# D. Implementați o metodă "afiseaza_detalii()" care să afișeze pe ecran toate detaliile despre student:
    # nume, vârstă, specializare și medie.
    def afiseaza_detalii(self):
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Specializare: {self.specializare}")
        print(f"Medie: {self.medie}")

# E. Implementați o metodă "este_promovat()" care să verifice dacă media studentului este mai mare sau egală cu 5.0
    # și să returneze un mesaj corespunzător, indicând dacă studentul este promovat sau nu.
    def este_promovat(self):
        if self.medie >= 5:
            print(f"Studentul {self.nume} este promovat.")
        else:
            print(f"Studentul {self.nume} nu este promovat.")



student1 = Student("Stroescu", 20, "IT", 8, 9, 10, 6, 5, 10)
print(f"Media studentului {student1.nume} este: {student1.calculeaza_medie()}.")
print("Detalii student:")
student1.afiseaza_detalii()
print()
student1.este_promovat()
print()

student2 = Student("Popescu", 22, "Limbi straine", 10, 5, 7, 10)
print(f"Media studentului {student2.nume} este: {student2.calculeaza_medie()}.")
print("Detalii student:")
student2.afiseaza_detalii()
print()
student2.este_promovat()






















