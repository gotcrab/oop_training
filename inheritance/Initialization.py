class Initialization:
    def __init__(self, capacity: int, food: list[str]):
        if type(capacity) == int and capacity >= 0:
            self.capacity = capacity
            self.food = food

        else:
            print('Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            if self.capacity == other:
                return True
            else:
                return False
        if isinstance(other, Initialization):
            if self.capacity == other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            if self.capacity < other:
                return True
            else:
                return False
        if isinstance(other, Initialization):
            if self.capacity < other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            if self.capacity > other:
                return True
            else:
                return False
        if isinstance(other, Initialization):
            if self.capacity > other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'


if __name__ == '__main__':
    one = Initialization(50, ['watermelon', 'bread', 'apples'])
    print(one.food)
    print(one.capacity)
    print(one.food[0])
    d = Vegetarian(600, ['potatoes', 'tomatoes'])
    print(d)
    m = MeatEater(152, ['eyes', 'noses', 'legs', 'eggs'])
    print(m)
    sth = SweetTooth(600, ['sweets', 'chocolate'])
    print(sth)
    print(sth > 5400)
    print(sth > 500)
    print(sth > 'a lot')
    print(sth == d)
    print(sth == one)
    print('-' * 50)

    v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
    print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
    v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
    m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
    print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
    s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
    print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
    print(s_first > v_first)  # True
    print(30000 == s_first)  # True
    print(s_first == 25000)  # False
    print(100000 < s_first)  # False
    print(100 < s_first)  # True
