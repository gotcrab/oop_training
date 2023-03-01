from functools import total_ordering

@total_ordering
class Rectangle:
    'compare areas of rectangles'
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area = self.height * self.width

    @property
    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        if isinstance(other, (int, float)):
            return self.area == other
        return 'nope. cant do this'

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other
        return 'nope. cant do this'

if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    assert r1.width == 3
    assert r1.height == 4
    assert r1.area == 12
    assert isinstance(type(r1).area, property), 'Вы не создали property area'

    assert r1 > 11
    assert not r1 > 12
    assert r1 >= 12
    assert r1 <= 12
    assert not r1 > 13
    assert not r1 == 13
    assert r1 != 13
    assert r1 == 12

    r2 = Rectangle(2, 6)
    assert r1 == r2
    assert not r1 != r2
    assert not r1 > r2
    assert not r1 < r2
    assert r1 >= r2
    assert r1 <= r2

    r3 = Rectangle(5, 2)
    assert not r2 == r3
    assert r2 != r3
    assert r2 > r3
    assert not r2 < r3
    assert r2 >= r3
    assert not r2 <= r3
    print('Good')