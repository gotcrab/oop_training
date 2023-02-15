class Person:
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        print("Get name")
        return self._name

    def _set_name(self, value):
        print("Set name")
        self._name = value

    def _del_name(self):
        print("Delete name")
        del self._name

    somecomand = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="работа обычного Property без декоратора"
    )

vasya = Person('Вася')
print(vasya.somecomand)
vasya.somecomand = 'Василий'
print(vasya.somecomand)
del vasya.somecomand
vasya.somecomand = 'VasIsDas'
print(vasya.somecomand)
print(help(vasya))
print('=' * 45)
print('=' * 45)


class SecPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        print("работа Проперти с декоратором")
        return self._name

    @name.setter
    def name(self, n):
        self._name = n
        print('сеттер имени с декоратором, теперь это', self._name)

    @name.deleter
    def name(self):
        print(f'Имя {self._name} удалено')
        del self._name

    @property
    def age(self):
        print("работа Проперти с декоратором")
        return self._age

halk = SecPerson('IAMHULK', 40)

print(halk.age)
print(halk.name)
halk.name = 'Володя'
print(halk.name)
del halk.name
