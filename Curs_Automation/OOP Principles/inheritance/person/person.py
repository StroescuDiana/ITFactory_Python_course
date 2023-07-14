import datetime

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def description(self):
        print("*" * 50)
        print(f"My name is {self.name}, I am {self.age}.")
        print(f"Address: {self.address}")

    def birthday(self):
        current_year = datetime.date.today().year
        return current_year - self.age
