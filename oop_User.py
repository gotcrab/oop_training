class User:
    def __init__(self, n, r):
        self.name = n
        self.role = r

class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role in Access.__access_list:
            return True
        return False

    @staticmethod
    def get_access(userr):
        if isinstance(userr, User) == False:
            print('AccessTypeError')

        elif Access.__check_access(userr.role) == True:
            print(f'User {userr.name}: success')
        elif Access.__check_access(userr.role) == False:
            print('AccessDenied')



user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError