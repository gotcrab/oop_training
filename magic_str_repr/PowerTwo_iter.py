class PowerTwo:
    def __init__(self, digit: int):
        self.digit = digit


    def __iter__(self):
        self.next_power = -1
        return self

    def __next__(self):
        if self.digit == self.next_power:
            raise StopIteration
        self.next_power += 1
        return 2 ** self.next_power

if __name__ == '__main__':
    numbers = PowerTwo(2)

    iterator = iter(numbers)

    print(next(iterator))  # печатает 1
    print(next(iterator))  # печатает 2
    print(next(iterator))  # печатает 4
    # print(next(iterator))  # исключение StopIteration

    iit = PowerTwo(8)
    for i in iit:
        print(i)