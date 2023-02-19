class UserMail:
    def __init__(self, log, mail):
        self.login = log
        self.__email = mail

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if value.count('@') == 1 and '.' in value and value.index('.') > value.index('@'):
            self.__email = value
        else:
            print(f'ErrorMail:{value}')

    email = property(fget=get_email, fset=set_email)


keks = UserMail('Maksim', 'fuuu@mail.ru')
print(keks.email)
keks.email = 'gogo@mail.ru'
print(keks.email)
