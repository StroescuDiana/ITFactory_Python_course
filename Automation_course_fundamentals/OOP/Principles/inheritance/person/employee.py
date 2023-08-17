from inheritance.person.person import Person

class Employee(Person):
    def __init__(self, name, age, address, company, salary):
        super().__init__(name, age, address)
        self.company = company
        self.salary = salary

    def description(self):
        super().description()
        print(f"Company: {self.company}\nSalary: {self.salary}")

    def annual_income(self):
        return self.salary * 12
