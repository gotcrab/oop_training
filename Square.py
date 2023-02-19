class Square:
    def __init__(self, side):
       self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


sq = Square(42)

# Считываем значения
print(sq.side)
print(sq.area)
# записаем новое значение
sq.area = 100
print(sq.side)