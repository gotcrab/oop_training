class CountInstancesMixin:
    count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.count += 1


class Cat(CountInstancesMixin):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Dog(CountInstancesMixin):
    def __init__(self, name):
        super().__init__()


obj1 = Cat("Барсик")
obj2 = Cat("Гипард")

obj3 = Dog("Жучка")

print(Cat.count)  # Output: 2
print(Dog.count)  # Output: 1