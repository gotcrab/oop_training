class NewInt(int):
    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(f'{self:b}')


if __name__ == '__main__':
    a = NewInt(9)
    print(a.repeat())
    d = NewInt(31)
    print(d.repeat())
    b = NewInt(NewInt(7) * NewInt(5))
    print(b.to_bin())
    c = NewInt(16)
    print(c.to_bin())
