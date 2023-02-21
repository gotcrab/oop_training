class File:
    def __init__(self, name, in_trash=False, is_deleted=False):
        self.name = name
        self.in_trash = in_trash
        self.is_deleted = is_deleted

    def restore_from_trash(self):
        '''
        печатает фразу «Файл {name} восстановлен из корзины»
        и проставляет атрибут in_trash в значение False
        :return: None
        '''
        if self in Trash.content:
            self.in_trash = False
            Trash.content.remove(self) # may be not self.name
            print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        '''
        печатает фразу «Файл {name} был удален» и проставляет
        атрибут is_deleted  в значение True
        :return: None
        '''
        if self in Trash.content:
            self.is_deleted = True
            self.in_trash = False
            Trash.content.remove(self)
            print(f'Файл {self.name} был удален')


    def read(self):
        '''
        печатает фразу «ErrorReadFileDeleted({name})»,
        если атрибут is_deleted истин, и выходит из метода
        печатает фразу «ErrorReadFileTrashed({name})»,
        если атрибут in_trash истин, и выходит из метода
        печатает фразу «Прочитали все содержимое файла {self.name}»
        если файл не удален и не в корзине
        :return: None
        '''
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return None
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return None
        print(f'Прочитали все содержимое файла {self.name}')
        return None

    def write(self, content):
        '''
        принимает значение content для записи и
        печатает фразу «ErrorWriteFileDeleted({name})»,
        если атрибут is_deleted истин, и выходит из метода
        печатает фразу «ErrorWriteFileTrashed({name})»,
        если атрибут in_trash истин, и выходит из метода
        печатает фразу «Записали значение {content} в файл {self.name}»,
        если файл не удален и не в корзине
        :param content: str
        :return: None
        '''
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return None
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return None
        print(f'Записали значение {content} в файл {self.name}')
        return None

class Trash:
    'Trash basket'
    content = []

    @staticmethod
    def add(file):
        '''
        принимает файл и сохраняет его в корзину:
        для этого нужно добавить его в атрибут content
        и проставить файлу атрибут in_trash значение True.
        Если в метод add передается не экземпляр класса File,
        необходимо вывести сообщение «В корзину добавлять можно только файл»
        :param file: str
        :return: None
        '''
        if isinstance(file, File):
            Trash.content.append(file)
            file.in_trash = True

        else:
            print('В корзину добавлять можно только файл')


    @staticmethod
    def clear():
        '''
        запускает процесс очистки файлов в корзине.
        Необходимо для всех файлов, хранящийся в атрибуте content,
        в порядке их добавления в корзину вызвать метод файла remove.
        Атрибут content  после очистки должен стать пустым списком.
        Сама процедура очистки должна начинаться фразой «Очищаем корзину»
        и заканчиваться фразой «Корзина пуста»
        :return: None
        '''
        print('Очищаем корзину')
        lst = []
        lst = Trash.content.copy()
        for i in lst:
            File.remove(i)

        if len(Trash.content) == 0:
            print('Корзина пуста')
        # else:
        #     raise ValueError('Something goes wrong. clear have a problem. Trash is not clear')

    @staticmethod
    def restore():
        '''
        запускает процесс восстановления файлов из корзины.
        Необходимо для всех файлов, хранящийся в атрибуте content,
        в порядке их добавления в корзину вызвать метод файла restore_from_trash.
        Атрибут content  после очистки должен стать пустым списком.
        Сама процедура восстановления должна начинаться фразой
        «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»
        :return: None
        '''
        print('Восстанавливаем файлы из корзины')

        lst = Trash.content.copy()
        for i in lst:
            if i in Trash.content:
                File.restore_from_trash(i)
        if len(Trash.content) == 0:
            print('Корзина пуста')


f1 = File('puppies.jpg')
Trash.add(f1)
f1.remove()
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)


