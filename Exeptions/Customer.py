class Customer:
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        self.check_type(value)

        if self.balance >= value:
            self.balance -= value
        else:
            raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        self.check_type(value)
        self.balance += value

if __name__ == '__main__':
    a = Customer('John', 150000)
    a.check_type(1500)
    print(a.balance)
    a.withdraw(145200)
    print(a.balance)
    a.deposit(480050)
    print(a.balance)
    a.deposit(123)
    print(a.balance)


