from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        self.ht = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        return self.ht.size

    def contains(self, element):
        return self.ht.contains(element)

    def add(self, element):
        if self.ht.contains(element):
            return False
        else:
            self.ht.set(element, element)
            return True

    def remove(self, element):
        self.ht.delete(element)

    def items(self):
        return self.ht.keys()

    def union(self, other_set):
        return Set(self.items() + other_set.items())

    def intersection(self, other_set):
        return Set([element for element in self.items() if other_set.contains(element)])

    def difference(self, other_set):
        new_set = Set()

        for item in self.ht.keys():
            if other_set.contains(item) == False:
                new_set.add(item)
        
        for item in other_set.ht.keys():
            if self.contains(item) == False:
                new_set.add(item)
        
        return new_set

    def is_subset(self, other_set):
        for item in other_set.items():
            if not self.contains(item):
                return False
        return True