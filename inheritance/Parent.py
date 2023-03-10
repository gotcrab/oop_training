class Parent:
    one = 1

class Chaild_one(Parent):
    two = 2

class Chaild_chaild(Chaild_one):
    three = 3

class Ch_4(Chaild_chaild):
    four = 4

if __name__ == '__main__':

    r = Chaild_chaild
    print(r.three)
    print(r.one)
    print(r.two)
    n = Ch_4
    print(n.one)