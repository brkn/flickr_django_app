class Stack:
    def __init__(self, data = [], maxsize=0):
        self._data = data
        self.maxsize = maxsize

    def __getitem__(self, indice):
        return self._data[indice]

    def __len__(self):
        return len(self._data)

    def push(self, element):
        if(len(self) == self.maxsize):
            self._data.pop(-1)
        self._data.insert(0, element)


recent_searches = Stack(maxsize=3)
print(recent_searches[1])