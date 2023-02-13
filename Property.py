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

    namename = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="Чё либо"
    )

pers = Person('Вася')
print(pers.namename)
pers.namename = 'Kkkk'
print(pers.namename)

print(help(pers))
