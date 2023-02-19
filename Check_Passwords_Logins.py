from string import digits
from string import ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        # transmit to setter
        self.password = password
        # transmit to setter

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if 5 > len(password) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = password

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt') as easy_p:
            for i in easy_p:
                if password == i.strip():
                    return True
            return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in ascii_letters and i not in digits:
                return False
        return True

    @staticmethod
    def is_include_all_register(password):
        for i in password:
            if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                for j in password:
                    if j in 'qwertyuiopasdfghjklzxcvbnm':
                        return True
        return False

    @staticmethod
    def is_include_digit(password):
        for i in password:
            if i in digits:
                return True
        return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        if login.count('@') != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' not in login:
            raise ValueError("Логин должен содержать символ '.'")
        if login.find('@') > login.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = login


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
# r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")
