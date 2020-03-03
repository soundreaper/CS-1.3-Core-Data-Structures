from binarytree import BinarySearchTree

f = open('/usr/share/dict/words', 'r')

wordList = []
for x in f.read().splitlines():
    wordList.append(x)

tree = BinarySearchTree(wordList)
print(tree.size)