class Fruit:
    'can compare fruits'

    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit) and self.price == other.price:
            return True

        if isinstance(other, (int, float)) and self.price == other:
            return True

        return False

    def __lt__(self, other):
        if isinstance(other, Fruit) and self.price < other.price:
            return True

        if isinstance(other, (int, float)) and self.price < other:
            return True

        return False

    def __le__(self, other):
        if isinstance(other, Fruit) and self.price <= other.price:
            return True

        if isinstance(other, (int, float)) and self.price <= other:
            return True

        return False

    def __gt__(self, other):
        if isinstance(other, Fruit) and self.price > other.price:
            return True

        if isinstance(other, (int, float)) and self.price > other:
            return True

        return False

    def __ge__(self, other):
        if isinstance(other, Fruit) and self.price >= other.price:
            return True

        if isinstance(other, (int, float)) and self.price >= other:
            return True

        return False


if __name__ == '__main__':
    apple = Fruit("Apple", 0.5)
    orange = Fruit("Orange", 1)
    banana = Fruit("Banana", 1.6)
    lime = Fruit("Lime", 1.0)

    assert (banana > 1.2) is True
    assert (banana >= 1.2) is True
    assert (banana == 1.2) is False
    assert (banana != 1.2) is True
    assert (banana < 1.2) is False
    assert (banana <= 1.2) is False

    assert (apple > orange) is False
    assert (apple >= orange) is False
    assert (apple == orange) is False
    assert (apple != orange) is True
    assert (apple < orange) is True
    assert (apple <= orange) is True

    assert (orange == lime) is True
    assert (orange != lime) is False
    assert (orange > lime) is False
    assert (orange < lime) is False
    assert (orange <= lime) is True
    assert (orange >= lime) is True
    print('Good')
