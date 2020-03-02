from sets import Set
import unittest

class SetTest(unittest.TestCase):
    def test_init(self):
        s = Set(['a','b','c'])
        assert s.ht is not None
        assert s.ht.length() == 3
        assert s.size() == 3
    
    def test_contains(self):
        s = Set(['a','b','c'])
        assert s.contains('a') == True
        assert s.contains('d') == False

    def test_add(self):
        s = Set()
        assert s.add('a') == True
        assert s.add('b') == True
        assert s.add('c') == True
        assert s.size() == 3

        assert s.add('b') == False

    def test_remove(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')

        s.remove('c')
        assert s.size() == 2

        s.remove('b')
        assert s.size() == 1

        s.remove('a')
        assert s.size() == 0

        with self.assertRaises(KeyError):
            s.remove('c')

    def test_union(self):
        s1 = Set(['a', 'b', 'c'])
        s2 = Set(['c', 'd', 'e'])
        s3 = s1.union(s2)
        assert s3.contains('a') == True
        assert s3.contains('b') == True
        assert s3.contains('c') == True
        assert s3.contains('d') == True
        assert s3.contains('e') == True
        assert s3.size() == 5

    def test_intersection(self):
        s1 = Set(['a', 'b', 'c'])
        s2 = Set(['b', 'c', 'd'])
        s3 = s1.intersection(s2)
        assert s3.contains('b') == True
        assert s3.contains('c') == True
        assert s3.size() == 2

    def test_difference(self):
        s1 = Set(['a', 'b', 'c', 'd'])
        s2 = Set(['c', 'd', 'e', 'f'])
        s3 = s1.difference(s2)
        assert s3.contains('a') == True
        assert s3.contains('b') == True
        assert s3.contains('e') == False
        assert s3.contains('f') == False
        assert s3.size() == 2

    def test_is_subset(self):
        s1 = Set(['a', 'b', 'c', 'd'])
        s2 = Set(['a', 'b'])
        s3 = Set(['b', 'd'])
        s4 = Set(['x', 'y'])

        assert s1.is_subset(s2) == True
        assert s1.is_subset(s3) == True
        assert s1.is_subset(s4) == False

if __name__ == '__main__':
    unittest.main()