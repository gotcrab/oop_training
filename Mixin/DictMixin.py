class DictMixin:
    def to_dict(self):
        return self.__dict__


class Phone(DictMixin):
    def __init__(self, number: str):
        self.number = number
        # self.number = self.number


class Address(DictMixin):
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Person(DictMixin):
    def __init__(self, name: str, age: int, address: Address):
        self.name = name
        self.age = age
        self.address = address.__dict__


class Company(DictMixin):
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address


if __name__ == '__main__':
    address = Address("123 Main St", "Anytown", "CA", "12345")
    john_doe = Person("John Doe", 30, address)
    # print(john_doe.to_dict())

    john_doe_dict = john_doe.to_dict()

    assert john_doe_dict == {
        'name': 'John Doe',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip_code': '12345'
        }
    }
    # print('ok')
    address = Address("123 Main St", "Albuquerque", "NM", "987654")
    assert address.to_dict() == {
        'street': '123 Main St',
        'city': 'Albuquerque',
        'state': 'NM',
        'zip_code': '987654'
    }
    walter = Person("Walter White", 30, address)
    assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                            'state': 'NM',
                                            'street': '123 Main St',
                                            'zip_code': '987654'},
                                'age': 30,
                                'name': 'Walter White'}
    walter_phone = Phone("555-1234")
    # walter.phone = walter_phone
    walter.phone = walter_phone.__dict__

    # print(walter_phone.__dict__)
    # print(walter.phone.__dict__)
    # print(walter.phone.to_dict())
    # print(walter.to_dict())

    assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                            'state': 'NM',
                                            'street': '123 Main St',
                                            'zip_code': '987654'},
                                'age': 30,
                                'name': 'Walter White',
                                'phone': {'number': '555-1234'}}

    company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
    company = Company("SCHOOL", company_address)

    assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                             'state': 'NM',
                                             'street': '3828 Piermont Dr',
                                             'zip_code': '12345'},
                                 'name': 'SCHOOL'}

    print('ok')

