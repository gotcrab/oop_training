class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):
    def is_employee(self):
        return True

if __name__ == '__main__':
    emp1 = Person("vasya")
    print(emp1.get_name(), emp1.is_employee())  # vasya False

    emp2 = Employee("gena bukin")
    print(emp2.get_name(), emp2.is_employee())  # gena bukin True

    assert issubclass(Employee, Person)

    p = Person("just human")
    assert p.name == 'just human'
    assert p.get_name() == 'just human'
    assert p.is_employee() is False

    emp = Employee("Geek")
    assert emp.name == 'Geek'
    assert emp.get_name() == 'Geek'
    assert emp.is_employee() is True
    print('Good')
