class WeatherStation:
    'Метеостанция, которая калибрует одновременно все датчики во всех ЭК'

    __shared_attr = {
        'temperature': 0,
        'humidity': 0,
        'pressure': 0
    }

    # формируем единый словарь атрибутов класса

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    # передаём в инициализатор ссылку на монословарь

    def update_data(self, t: int, h: int, p: int) -> None:
        'задаём параметры у всех ЭК'
        self.temperature = t
        self.humidity = h
        self.pressure = p

    def get_current_data(self) -> tuple:
        'возвращаем кортеж показаний'
        return (self.temperature, self.humidity, self.pressure)


# код для проверки
sensor1 = WeatherStation()
assert sensor1.temperature == 0
assert sensor1.humidity == 0
assert sensor1.pressure == 0
sensor2 = WeatherStation()
assert sensor2.get_current_data() == (0, 0, 0)
sensor1.update_data(25, 60, 103)
assert sensor1.get_current_data() == (25, 60, 103)
assert sensor2.get_current_data() == (25, 60, 103)
sensor3 = WeatherStation()
assert sensor3.get_current_data() == (25, 60, 103)
sensor3.update_data(50, 20, 10)
assert sensor1.get_current_data() == (50, 20, 10)
assert sensor2.get_current_data() == (50, 20, 10)
print('Good')
