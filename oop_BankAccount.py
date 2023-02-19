class BankAccount:
    bank_name = "Tinkoff Bank"
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        return cls (name, balance)

    @classmethod
    def bank_info(cls):
        return f'{BankAccount.bank_name} is located in {BankAccount.address}'

oleg = BankAccount.create_account("Олег Тинкофф", 1000)
assert isinstance(oleg, BankAccount)
assert oleg.name == 'Олег Тинкофф'
assert oleg.balance == 1000
assert BankAccount.bank_info() == 'Tinkoff Bank is located in Москва, ул. 2-я Хуторская, д. 38А'

ivan = BankAccount.create_account("Ivan Reon", 50)
assert isinstance(ivan, BankAccount)
assert ivan.name == 'Ivan Reon'
assert ivan.balance == 50
print('Good')