# Tuples

# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
d = {'a' : 10, 'c' : 22, 'b' : 1}

# First we sort the dictionary by the key using the items() method and sorted() function
print(d.items())
# print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k,v)


# We can also sort the dictionary by the value instead, by creating a new list and swapping the position of the key-value pair in the new list
tmp = list()
for k,v in d.items():
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# Count the top 10 words with the most appearances in an input file
fhandle = open('sample.txt')
d2 = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        d2[word] = d2.get(word, 0) + 1
'''
newlist = list()
for k,v in d2.items():
    newlist.append((v,k))
newlist = sorted(newlist, reverse=True)
'''

# We can simplify the above code by using List Comprehension logic
newlist = sorted( [ (v,k) for k,v in d2.items() ], reverse=True )

for val, key in newlist[:10]:
    print(key, val)