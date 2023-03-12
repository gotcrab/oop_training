class Transport:
    'describe vehicles characteristics'
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'

class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, liters):
        if type(liters) != int:
            return print('Ошибка заправки автомобиля')
        self.__gasoline_residue += liters
        return print(f'Объем топлива увеличен на {liters} л и составляет {self.__gasoline_residue} л')

class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'

class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'

if __name__ == '__main__':
    bmw = Car ('BMW', 230, 99000, 450)
    print(bmw.gasoline)
    print(bmw.kind)
    print(bmw.brand)
    print(bmw.mileage)
    bmw.gasoline = 50
    print(bmw.gasoline)
    bmw.gasoline = 113
    print(bmw.gasoline)
    b = Boat('TOYBOTA', 100, 'Alexander Kuznetsov')
    print(b)
    print(b.max_speed)
    print(bmw)
    p = Plane('MIG-29', 900, 1)
    print(p)
    transport = Transport('Telega', 10)
    print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
    bike = Transport('shkolnik', 20, 'bike')
    print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

    first_plane = Plane('Virgin Atlantic', 700, 450)
    print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
    first_car = Car('BMW', 230, 75000, 300)
    print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
    print(first_car.gasoline)  # Осталось бензина на 300 км
    first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
    print(first_car.gasoline)  # Осталось бензина на 320 км
    second_car = Car('Audi', 230, 70000, 130)
    second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
    first_boat = Boat('Yamaha', 40, 'Petr')
    print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

