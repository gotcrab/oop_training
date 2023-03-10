class Vector:
    'return sorted coords of vector'
    def __init__(self, *args):
        values = []
        for i in args:
            if isinstance(i, int):
                values.append(int(i))
        self.values = values
        # print(self.values)


    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'
        return f'Пустой вектор'

    def __add__(self, other):
        if type(other) == int:
            new_val = []
            for i in self.values:
                new_val.append(i + other)
            return Vector(*new_val)
        if isinstance(other, Vector):
            if sorted(self.values) == sorted(other.values):
                new_val = []
                for i in sorted(self.values):
                    new_val.append(i * 2)
                return Vector(*new_val)
            else:
                return 'Сложение векторов разной длины недопустимо'
        return f'Вектор нельзя сложить с {other}'

    def __mul__(self, other):
        if type(other) == int:
            new_val = []
            for i in self.values:
                new_val.append(i * other)
            return Vector(*new_val)
        if isinstance(other, Vector):
            if sorted(self.values) == sorted(other.values):
                new_val = []
                for i in sorted(self.values):
                    new_val.append(i ** 2)
                return Vector(*new_val)
            else:
                return 'Умножение векторов разной длины недопустимо'
        return f'Вектор нельзя умножать с {other}'




#tests:

v1 = Vector(2, 3, 1)
assert isinstance(v1, Vector)
assert str(v1) == 'Вектор(1, 2, 3)'

v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'

v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'

v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []

print(v1)
print(v2)
print(v3)
print(v4)

v5 = v1 + 2
print(v5)

v6 = v1 + 'Hello'
print('v6 =', v6)

v7 = v1 * True
print('v7 =', v7)
