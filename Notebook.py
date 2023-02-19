class Notebook:
    def __init__(self, lst: list):
        self._notes = lst

    @property
    def notes_list(self):
        for i, j in enumerate(self._notes, 1):
            print(f'{i}.{j}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list