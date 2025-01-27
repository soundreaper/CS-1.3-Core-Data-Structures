import sys

'''
The below code would load and return a list of the built-in Mac dictionary.
'''
# def getDictionary():
#     with open('/usr/share/dict/words') as f:
#       d_raw = f.read()
#     d_list = d_raw.split("\n")
#     return d_list

'''
The method below returns a 26-dimension vector that counts the frequency of each letter in a given string.
'''    
def wordToDictionary(word):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    word = word.lower()
    wordList = list(word)
    for i in range(0, len(wordList)):
        if wordList[i] in letters:
            ind = letters.index(wordList[i])
            vector[ind] += 1
    return vector

'''
The method below converts the vector from the above function into a 4-bit integer.
'''
def vectorToInt(vector):
    power = 0
    num = 0
    for i in range(0, len(vector)):
        temp = (vector[i]*(2**power))
        num += temp
        power += 4
    return num
    
'''
The below code was used to generate the dict.txt file in the same directory which contains integer
keys with the words from the dictionary as values. Since the dictionary has already been generated
we don't need the below code to be active unless we need to re-generate the dictionary.
'''    
# def intToDict(dict):
#     d = {}
#     for i in range(0, len(dict)):
#         v = wordToDictionary(dict[i])
#         Int = vectorToInt(v)
#         if Int in d:
#             tat = d.get(Int)
#             tat.append(dict[i])
#             d[Int] = tat
#         elif Int not in d:
#             d[Int] = [dict[i]]
#     return d
        
# d = getDictionary()
# ind = intToDict(d)
# g = open("dict.txt","w")
# g.write(str(ind))
# g.close()

'''
We open the generated dictionary below and read it in as a python dictionary.
'''
generatedDictionary = open("dict.txt", "r")
ind = eval(generatedDictionary.read())

'''
We take scrambled words as command line arguments and then convert them to integers and attempt to
match them to the dictionary above.
'''
for x in sys.argv[1:]:
    v = vectorToInt(wordToDictionary(str(x)))
    unscrambled = ind.get(v, 'Word Not in Dictionary.')
    print(unscrambled)