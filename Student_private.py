class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'''Имя: {self.__name}
Возраст: {self.__age}
Направление: {self.__branch}''')
    def access_private_method(self):
        self.__display_details()

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()
