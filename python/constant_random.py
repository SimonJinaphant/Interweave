from random import randrange


class RandomDictionary():
    """
    A data structure which supports insert(), remove(), contains(), and random() in O(1) time
    """

    def __init__(self):
        self.value_indices = {}
        self.values = []

    def __contains__(self, value):
        return value in self.value_indices

    def insert(self, value):
        self.value_indices[value] = len(self.values)
        self.values.append(value)

    def random(self):
        random_index = randrange(len(self.values))
        return self.values[random_index]

    def remove(self, value):
        if value not in self.value_indices:
            return

        index = self.value_indices[value]
        del self.value_indices[value]

        tail_index = len(self.values)-1
        tail_element = self.values[tail_index]

        self._swap_values(index, tail_index)
        self.values.pop()

        if tail_index != index:
            self.value_indices[tail_element] = index

    def _swap_values(self, i, j):
        temp = self.values[j]
        self.values[j] = self.values[i]
        self.values[i] = temp
