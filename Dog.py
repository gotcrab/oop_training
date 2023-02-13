class Dog:
    def __init__(self, name='Какой-либо Тузик', age='пока живой'):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound='Ифь'):
        self.sound = sound
        return f'{self.name} says {self.sound}'

sharik = Dog('Шарик', '2 годика')
print(sharik.name)
print(sharik.age)

jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

julia = Dog('Жуля', 4)
julia.speak('Уууууу')

print(julia.description())
print(julia.speak('Уууу'))