from string import digits


class BankUser:
    '''create a bank user with a login and a password.
    Check user's password for length, digit inside and belonging to string'''
    def __init__(self, log, pas):
        self.login = log
        self.password = pas
        # this is already the setter!
        # Not the class attribute!
        # password saving in self.__password in SETTER! not here!
        self.__secret_message = 'WORLD LOVE YOU <3'

    @property
    def secret(self):
        '''
        Check access to the secret message.
        If your password correct, your will seen the secret)
        :return: str
        '''
        s = input('Please, insert your password: ')
        if s == self.password:
            return self.__secret_message
        else:
            raise ValueError('Alarm! Access DENIED!')


    @property
    def password(self):
        print('this is getter')
        return self.__password

    @staticmethod
    def is_dig_inside(pswrd):
        '''
        we can create it outside the class BankUser.
        But also can create it here.
        If we create it here, we need to use staticmetod,
        cause this function will be take only 1 argument - password
        oh, ye, it's docstring)
        check digits inside a password
        '''
        for i in pswrd:
            if i in digits:
                return True
        return False

    @password.setter
    def password(self, newpas):
        'just setter with some checks'
        print('setter is working')
        if not isinstance(newpas, str):
            raise TypeError('password must be a string')
        if len(newpas) < 4:
            raise ValueError('password is too short, minimum 4 characters needs')
        if len(newpas) > 12:
            raise ValueError('password is too long, maximum 12 characters needs')
        if not BankUser.is_dig_inside(newpas):
            raise ValueError('password must have minimum 1 digit')
        # if newpas in
        self.__password = newpas
        print('password was changed')


firstman = BankUser('Ivan', 'gggdf0')
print(firstman.password)
firstman.password = '1rtyutyui'
print(firstman.password)
firstman.password = 'Qwerty1234'

print(firstman.secret)
