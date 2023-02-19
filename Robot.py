class Robot:
    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

    def set_name(self, n):
        self.name = n


c3po = Robot()
r2d2 = Robot()

c3po.set_name('C3PO')
print(c3po.__dict__)
c3po.say_hello()
c3po.say_bye()
r2d2.say_hello()
r2d2.say_bye()
