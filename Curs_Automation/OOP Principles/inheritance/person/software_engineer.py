import datetime
from inheritance.person.employee import Employee

class SoftwareEngineer(Employee):
    def __init__(self, name, age, address, company, salary, years_of_experience):
        if "Telenav" in company and datetime.datetime.today().date() >= datetime.date(2023, 5, 1):
            raise Exception("Are you sure? I don't think so.")
        super().__init__(name, age, address, company, salary)
        self.years_of_experience = years_of_experience

    def description(self):
        super().description()
        print(self.years_of_experience)
