import json

class JsonSerializableMixin:

    def to_json(self):
        return json.dumps(self.__dict__)


class Person(JsonSerializableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Car(JsonSerializableMixin):
    def __init__(self, make: str, color: str):
        self.make = make
        self.color = color


class Book(JsonSerializableMixin):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

if __name__ == '__main__':

    person = Person("John", 30)
    print(person.to_json())

    b1 = Book('Wars never changes', 'Fallout')
    print(b1.to_json())
    car = Car("Toyota", "red")

    print(car.to_json())
    assert car.to_json() == '{"make": "Toyota", "color": "red"}'

    book = Book("The Catcher in the Rye", "J.D. Salinger")
    assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
    book.ratings = [5, 4, 5, 4, 5]
    book.is_bestseller = True
    book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'

    person = Person("John", 30)
    assert person.to_json() == '{"name": "John", "age": 30}'
    print('Good')