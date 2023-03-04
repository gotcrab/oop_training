class Building:
    """
    Creates buildings and puts companies to the floor
    """
    def __init__(self, floors):
        self.floors = [None for i in range(floors)]

    def __getitem__(self, item: int):
        if 0 <= item < len(self.floors):
            return self.floors[item]
        raise IndexError ('index is out of range')

    def __setitem__(self, key: int, value: str):
        if 0 <= key < len(self.floors):
            self.floors[key] = value
        else:
            raise IndexError ('index is out of range')

    def __delitem__(self, key: int):
        if 0 <= key < len(self.floors):
            self.floors[key] = None
        else:
            raise IndexError ('index is out of range')

if __name__ == '__main__':
    iron_building = Building(22)  # Создаем здание с 22 этажами
    iron_building[0] = 'Reception'
    iron_building[1] = 'Oscorp Industries'
    iron_building[2] = 'Stark Industries'
    print(iron_building[2])
    print(iron_building[1])
    print(iron_building[0])
    del iron_building[2]
    print(iron_building[2])


