class File:
    def __init__(self, name, in_trash=False, is_deleted=False):
        self.name = name
        self.in_trash = in_trash
        self.is_deleted = is_deleted

    def restore_from_trash(self):
        if self in Trash.content:
            self.in_trash = False
            Trash.content.remove(self.name) # may be not self.name
            print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        if self in Trash.content:
            self.is_deleted = True
            Trash.content.remove(self)
            print(f'Файл {self.name} был удален')


    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return None
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return None
        print(f'Прочитали все содержимое файла {self.name}')
        return None

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return None
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return None
        print(f'Записали значение {content} в файл {self.name}')
        return None

class Trash:
    content = []

    @staticmethod
    def add(file):

        if isinstance(file, File):
            Trash.content.append(file)
            # print(f'file.in_trash = {file.in_trash}')
            file.in_trash = True
            file.is_deleted = True
            # print(f'file.in_trash = {file.in_trash}')

        else:
            print('В корзину добавлять можно только файл')


    @staticmethod
    def clear():
        '''
        статик-метод  clear, который запускает процесс очистки файлов в корзине.
        Необходимо для всех файлов, хранящийся в атрибуте content,
        в порядке их добавления в корзину вызвать метод файла remove.
        Атрибут content  после очистки должен стать пустым списком.
        Сама процедура очистки должна начинаться фразой «Очищаем корзину»
        и заканчиваться фразой «Корзина пуста»
        :return:
        '''
        print('Очищаем корзину')
        lst = []
        lst = Trash.content.copy()
        for i in lst:
            File.remove(i)

        if len(Trash.content) == 0:
            print('Корзина пуста')
        else:
            raise ValueError('Something goes wrong. clear have a problem. Trash is not clear')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        lst = []
        lst = Trash.content.copy()
        for i in lst:
            File.restore_from_trash(i)
        if len(Trash.content) == 0:
            print('Корзина пуста')
        else:
            raise ValueError('Something goes wrong. restore have a problem. Trash is not clear')

f5 = 0
Trash.add(f5)
f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)
# f1.remove()

Trash.add(f2)
Trash.add(passwords)
print(Trash.content)
Trash.clear() # после этой команды вывод должен быть таким
# '''
# Очищаем корзину
# Файл puppies.jpg был удален
# Файл cat.jpg был удален
# Файл pass.txt был удален
# Корзина пуста
# '''
print(Trash.content)
f1.read() # ErrorReadFileTrashed(puppies.jpg)
Trash.add(f5)


