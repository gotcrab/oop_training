from collections import defaultdict
class Product:
    'class for description goods'
    def __init__(self, name: str, price: int | float) -> None:
        self.name = name
        self.price = price

class User:
    'about users in internet shop'
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        'return information about user and balance'
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self) -> int | float:
        'getter'
        return self.__balance

    @balance.setter
    def balance(self, balance):
        'setter'
        self.__balance = balance

    def deposit(self, plus_to_b):
        'input your deposite to balance'
        self.__balance += plus_to_b

    def payment(self, minus_b):
        'minus from your balance'
        if self.__balance >= minus_b:
            self.__balance -= minus_b
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False

class Cart:
    'Put your goods here'
    def __init__(self, user: User):
        '''
        принимающий на вход экземпляр класса User.
        Его необходимо сохранить в атрибуте user.
        Помимо этого метод  должен создать атрибут goods - пустой словарь
        (лучше использовать defaultdict). Он нужен будет для хранения наших товаров
        и их количества(ключ словаря - товар, значение - количество). И еще нам
        понадобится создать защищенный атрибут .__total со значением 0. В нем будет
        хранится итоговая сумма заказа
        :param user: User
        '''
        if isinstance(user, User):
            self.user = user
            self.goods = {}  # this is the basket
            self.__total = 0  # total price
        else:
            print('something wrong with __init__')

    def add(self, product: Product, goods_count: int | float = 1):
        '''
        принимает на вход экземпляр класса Product и необязательный аргумент количество
        товаров (по умолчанию 1). Метод add  должен увеличить в корзине (атрибут goods)
        количество указанного товара  на переданное значение количество и пересчитать
        атрибут self.__total
        :return:
        '''
        if isinstance(product, Product):
            if product in self.goods:
                self.goods[product] += goods_count
            else:
                self.goods[product] = goods_count # or may be just product
            self.__total += product.price * goods_count



        pass
    def remove(self, product: Product, goods_count=1):
        '''
        принимает на вход экземпляр класса Product и необязательный аргумент количество
        товаров (по умолчанию 1).  Метод remove  должен уменьшить в корзине (атрибут goods)
        количество указанного товара  на переданное значение количество и пересчитать атрибут
        self.__total. Обратите внимание на то, что количество товара в корзине не может
        стать отрицательным как и итоговая сумма
        :return:
        '''
        if isinstance(product, Product):
            if goods_count < self.goods[product]:
                self.goods[product] = self.goods[product] - goods_count
                self.__total -= product.price * goods_count
            else:
                self.__total -= product.price * self.goods[product]
                del self.goods[product]



    @property
    def total(self):
        return self.__total


    def order(self):
        '''
        должен использовать метод payment  из класса User и передать в него итоговую сумму
        корзины. В случае, если средств пользователю хватило, вывести сообщение
        «Заказ оплачен», в противном случае - «Проблема с оплатой»;
        :return:
        '''

        if self.__total <= self.user.balance:
            self.user.payment(self.__total)
            print('Заказ оплачен')
        else:
            self.user.payment(self.__total)
            print('Проблема с оплатой')



    def print_check(self):
        '''
        печатающий на экран чек. Он должен начинаться со строки
        ---Your check---
        Затем выводится состав корзины в алфавитном порядке по названию товара в виде
        {Имя товара} {Цена товара} {Количество товара} {Сумма}
        И заканчивается чек строкой
        ---Total: {self.total}---
        :return: str
        '''
        print('---Your check---')
        for i, j in sorted(self.goods.items(), key=lambda x: (x[0].name, x[1])):
            print(i.name, i.price, j, i.price * j)
        print(f'---Total: {self.__total}---')




apple = Product('Apples', 50)
orange = Product('Portakal', 75)
fish = Product('Balik', 80)
bread = Product('Ekmek', 5)
olive = Product('Olives', 80)
cheese = Product('Parmezan', 250)

rrr = User('Grom', 2000)

f1 = Cart(rrr)
f1.add(apple, 5)
f1.add(cheese, 2)
f1.add(olive, 2)

f1.remove(apple, 1)
f1.order()


print(f1.__dict__)
print(f1.goods)
print(f1.total)
print(f1.print_check())

print('0' * 50)

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
cart_billy.add(lemon, 3)
cart_billy.print_check()
cart_billy.remove(lemon, 6)
cart_billy.print_check()
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
cart_billy.order()
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20




