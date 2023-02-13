class Counter:
    'счётчик'

    def start_from(self, n=0):
        'начинает отсчёт от числа n'
        self.cnt = n

    def increment(self):
        self.cnt += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.cnt}')

    def reset(self):
        self.cnt = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.increment()
c1.increment()

c1.display()

c2 = Counter()
c2.start_from(5)
c2.increment()

c2.display()
c1.display()
c2.reset()
c2.display()
c1.display()
c2.increment()
c2.display()

