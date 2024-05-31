# Dictionaries
'''
names = ['pablo', 'sergio', 'raul', 'mikel', 'mikel', 'sergio', 'kike']
dict = {}

for name in names:
    dict[name] = dict.get(name, 0) + 1

# for key in dict:
#     print(dict[key])

# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))

dictlist = list(dict)
# print(dictlist)

dictitems = list(dict.items())
for t in dictitems:
    print(type(t))
'''

####################################  Unit Final Exercise  ####################################

fhandle = open('sample.txt')
dict = dict()

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    # print(words)
    for word in words:
        dict[word] = dict.get(word, 0) + 1

print(dict)
mostword = None
maxcount = None
for key, value in dict.items(): # This generates a Tuple for each key-value pair.
    # print(key, value)
    if mostword is None or maxcount < value:
        mostword = key
        maxcount = value

print(mostword, maxcount)

