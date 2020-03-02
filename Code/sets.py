from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        self.ht = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        return self.ht.size

    # Time Complexity: O(1) using a HashTable.
    def contains(self, element):
        return self.ht.contains(element)

    # Time Complexity: O(1) using a HashTable.
    def add(self, element):
        if self.ht.contains(element):
            return False
        else:
            self.ht.set(element, element)
            return True

    # Time Complexity: O(1) using a HashTable.
    def remove(self, element):
        self.ht.delete(element)

    def items(self):
        return self.ht.keys()

    # Time Complexity: O(n) since it relies on the size of the first and second set.
    def union(self, other_set):
        return Set(self.items() + other_set.items())

    # Time Complexity: O(n) since it relies on the size of the first set.
    def intersection(self, other_set):
        return Set([element for element in self.items() if other_set.contains(element)])

    # Time Complexity: O(n) since it relies on the size of the first set.
    def difference(self, other_set):
        # sorry I said u were wrong Ben ur code is god my bad
        return Set([element for element in self.items() if not other_set.contains(element)])
        
        # new_set = Set()

        # for item in self.ht.keys():
        #     if other_set.contains(item) == False:
        #         new_set.add(item)
        
        # for item in other_set.ht.keys():
        #     if self.contains(item) == False:
        #         new_set.add(item)
        
        # return new_set

    # Time Complexity: O(n) since it relies on the size of the set we are checking.
    def is_subset(self, other_set):
        for item in other_set.items():
            if not self.contains(item):
                return False
        return True