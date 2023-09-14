# assignment: Hashtable

# author: Will Sobolewski
# date: Aug 2nd, 2023
# file: Hashtable.py contains the class Hashtable for making Hashtables
# input: list of strings
# output: hashtable of the strings, and assertion statements to validate the hashtable class implementation

class Hashtable:
    def __init__(self, size=8):
        self.table = [[] for _ in range(size)]
        self.size = size
        self.num_elements = 0

    def _hash(self, key):
        return hash(key) % self.size

    def get(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def get_size(self):
        return self.size

    def add(self, key, value):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])
        self.num_elements += 1

    def remove(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                self.table[index].remove(kv)
                self.num_elements -= 1
                return

    def is_empty(self):
        return self.num_elements == 0

    def __len__(self):
        return self.num_elements


if __name__ == '__main__':

    data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

    # make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc.
    h = Hashtable()
    for i in range(len(data)):
        h.add(data[i], i)       # the key is data[i], the value is i

    # print the hash table items
    for key in data:
        print(h.get(key))

    # test the method get() and if items in the hash table are correct
    for i in range(len(data)):
        assert h.get(data[i]) == i

    # test the method get_size()
    n = h.get_size()  # returns the size of the hash table array
    assert n == 8
    assert len(h) == 8  # returns the number of items in the hash table

    # test the method remove() and is_empty()
    for i in data:
        h.remove(i)
    print(h.is_empty())
    assert h.is_empty()
    assert len(h) == 0
    assert h.get_size() == 8
