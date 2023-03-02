class Addition:

    def __call__(self, *args):
        s = sum([i for i in args if type(i) == int or type(i) == float])
        return f'Сумма переданных значений = {s}'


if __name__ == '__main__':
    a = Addition()
    print(a(1, 2, 3, True, 5.5, 'asck', [1, 2, 2, 3], (4, 4, 4)))
    print(a(1, 2))
