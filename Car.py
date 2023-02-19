class Car:

    def __init__(self, x, engine):
        self.__model = x
        self.engine = engine

    @classmethod
    def add_car(cls, m='Mercedes', e=2.0):
        return cls(m, e)

    @property
    def getcar(self):
        return self.__model, self.engine


car1 = Car.add_car('Запорожец')
print(car1.getcar)

car2 = Car.add_car('BMW', 5.0)
print(car2.getcar)

car3 = Car.add_car()
print(car3.getcar)
