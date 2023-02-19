class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')

class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')

class Employee:
    def __init__(self, name, age, company_name, location):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.location = location
        self.personal_data = Person(self.name, self.age)
        self.work = Company(self.company_name, self.location)




emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()

print('-' * 45)

july = Employee('Собака Жуля', '4 годика', 'Косточки-ин-да-Хаус', 'Мытищи')
eva = Employee('Игрушечная Собачка Ева', '2 годика', 'Магазин игрушечных собачек', 'Зеленоград')

july.personal_data.display_person_info()
july.work.display_company_info()

eva.personal_data.display_person_info()
eva.work.display_company_info()

