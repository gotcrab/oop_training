class WeatherStation:

    __shared_attr = {
        'one': 1,
        'two': 2,
        'three': 3
    }
    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr
