"""méthodes de list"""
from copy import deepcopy

class Liste():
    def __init__(self, liste):
        self.liste = liste

    def __repr__(self):
        return str(self.liste)

    def __bool__(self):
        return len(self.liste) != 0

    def __len__(self):
        return len(self.liste)

    def __getitem__(self, i):
        return self.liste[i]

    def __setitem__(self, i, item):
        self.liste[i] = item

    def copy(self):
        return Liste(deepcopy(self.liste))

    def reset(self):
        self.liste = []

    def append(self, x):
        self.liste += [x]

    def pop(self, i=-1):
        last_element = self[i]
        self.liste = self[:i]
        return last_element

    def extend(self, liste2):
        self.liste = self.liste + liste2

    def insert(self, i, x):
        self.liste = self.liste[:i] + [x] + self.liste[i:]

    def index(self, x):
        for i in range(len(self)):
            if self.liste[i] == x:
                return i
        raise Exception(f'{x} is not in list')

    def remove(self, x):
        self.liste.pop(self.liste.index(x))

    def count(self, x):
        count = 0
        for element in self.liste:
            if element == x:
                count += 1
        return count

    def max(self):
        if self.liste:
            max = self[0]
            for element in self.liste:
                if element > max:
                    max = element
            return max

    def min(self):
        if self.liste:
            min = self[0]
            for element in self.liste:
                if element < min:
                    min = element
            return min

    def sort(self):
        temp = self.copy()
        self.liste = []
        while temp:
            min = temp.min()
            temp.remove(min)
            self.append(min)

    def reverse(self):
        temp = self.copy()
        self.liste = []
        for i in range(len(temp)):
            self.append(temp[-i-1])

    def search(self, x):
        out = []
        for i in range(len(self.liste)):
            if self[i] == x:
                out.append(i)
        return out

    def delete(self, x):
        for i in range(self.count(x)):
            self.remove(x)

a = Liste([1, 2, 4, 1, 3, 1])