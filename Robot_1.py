class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {self.name} был создан')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{Robot.population}, вот сколько нас еще осталось')

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
Robot.how_many()
droid1 = Robot("R2-D2")
assert droid1.name == 'R2-D2'
assert Robot.population == 1
droid1.say_hello()
Robot.how_many()
droid2 = Robot("C-3PO")
assert droid2.name == 'C-3PO'
assert Robot.population == 2
droid2.say_hello()
Robot.how_many()
droid1.destroy()
assert Robot.population == 1
droid2.destroy()
assert Robot.population == 0
Robot.how_many()