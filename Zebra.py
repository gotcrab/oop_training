class Zebra:
    def __init__(self, step = 0):
        self.step = step

    def which_stripe(self):
        if self.step % 2:
            print("Полоска черная")
            self.step += 1
        else:
            print("Полоска белая")
            self.step += 1

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"