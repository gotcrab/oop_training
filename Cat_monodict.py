class Cat:
    __shared_attr = {      # Формирование единого словаря атрибутов класса
        'breed': 'pers',   # При изменении значений - эти значения обновятся
        'color': 'black'   # во всех экземплярах класса
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr  # Передаём в инициализатор ссылку на
                                           # созданный моно-словарь


cat1 = Cat()
cat2 = Cat()
print(cat1.__dict__)  # Проверим словарь атрибутов ЭК cat1
print(cat2.__dict__)
cat1.breed = 'дворовый кот'
cat2.color = 'orange'
print(cat1.__dict__)  # Проверим словарь атрибутов ЭК cat1
print(cat2.__dict__)