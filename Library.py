class Library:
    'Библиотека'

    def __init__(self, lst: list) -> None:
        self.__books = lst

    def __check_availability(self, book_name: str) -> bool:
        'принимает название книги и возвращает True, если книга присутствует в библиотеке, в противном случае возвращается False'
        if book_name in self.__books:
            return True
        return False

    def search_book(self, book_name: str) -> None:
        'ищет книгу в библиотеке при помощи приватного метода check_availability. Возвращает True, если нашел,  иначе False'
        return self.__check_availability(book_name)

    def return_book(self, book_name: str) -> None:
        'принимает название книги, которую нужно вернуть в библиотеку. И добавляет её, соответственно'
        self.__books.append(book_name)

    def _checkout_book(self, book_name) -> bool:
        'Если книга имеется в наличии возврращает True и выдаёт книгу читателю. Из библиотеки удаляет. Если книга отсутствовала, вернёт False'
        if book_name in self.__books:
            self.__books.remove(book_name)
            return True
        return False


library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')
