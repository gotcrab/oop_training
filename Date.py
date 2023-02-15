class Date:
    def __init__(self, d, m, y):
        self._day = d
        self._month = m
        self._year = y

    @property
    def date(self):
        return f'{self._day:02}/{self._month:02}/{self._year:04}'

    @property
    def usa_date(self):
        return f'{self._month:02}-{self._day:02}-{self._year:04}'

d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999