class PasswordInvalidError(Exception):
    pass

class PasswordLengthError(PasswordInvalidError):
    pass

class PasswordContainUpperError(PasswordInvalidError):
    pass

class PasswordContainDigitError(PasswordInvalidError):
    pass

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, password):
        self.check_password_length(password)
        self.check_password_upper(password)
        self.check_password_digit(password)

        self.password = password

    @staticmethod
    def check_password_length(password):
        if len(password) < 8:
            raise PasswordLengthError('Пароль должен быть не менее 8 символов')

    @staticmethod
    def check_password_upper(password: str):
        for i in password:
            if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                return None
        raise PasswordContainUpperError('Пароль должен содержать хотя бы одну заглавную букву')

    @staticmethod
    def check_password_digit(password):
        for i in password:
            if i in '0123456789':
                return None
        raise PasswordContainDigitError('Пароль должен содержать хотя бы одну цифру')

if __name__ == '__main__':
    a = User('Bob')
    a.set_password('qwelkj0F')
    print(a.password)

    assert issubclass(PasswordInvalidError, Exception)
    assert issubclass(PasswordLengthError, PasswordInvalidError)
    assert issubclass(PasswordContainUpperError, PasswordInvalidError)
    assert issubclass(PasswordContainDigitError, PasswordInvalidError)

    user = User("johndoe")

    try:
        user.set_password("weakpwd")
    except PasswordLengthError as e:
        print(e)

    try:
        user.set_password("strongpassword8")
    except PasswordContainUpperError as e:
        print(e)

    try:
        user.set_password("Safepassword")
    except PasswordContainDigitError as e:
        print(e)

    user.set_password("SecurePass123")
    assert user.password == 'SecurePass123'

    print('Good')

