class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        if self.file.readline().strip():
            return self.file.readline().strip()
        self.file.close()
        raise StopIteration


for line in FileReader('lorem.txt'):
    print(line)