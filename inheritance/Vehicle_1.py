class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.milage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):
    def __init__(self, name, mileage, capacity=4):
        super().__init__(name, mileage, capacity)

    def fare(self):
        return super().fare() * 1.35


if __name__ == '__main__':
    f = Taxi('vaz', 99999, 5)
    print(f.fare())

    sc = Vehicle('Scooter', 100, 2)
    sc.display()

    merc = Bus("Mercedes", 120000)
    merc.display()

    polo = Taxi("Volkswagen Polo", 15000)
    polo.display()

    t = Taxi('x', 111)
    print(t.__dict__)
