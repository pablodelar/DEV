# Handling files in Python
import pickle # For object serialization

filename = '/Users/oihane/Documents/Pablo/Python/sample.txt'
output_filename = '/Users/oihane/Documents/Pablo/Python/output.txt'

num = 5
l = [1, 2, 3]
d = {'a': 1, 'b': 2}

try:
    # with open(filename, 'r') as myfile:
        # for line in myfile:
    fhandle = open(filename, 'r')
    #help(fhandle)
    #print(dir(fhandle))
    print(type(fhandle))
except:
    print('File provided does not exist')
    quit() # If we don't add quit(), the program will continue its execution

fhandle2 = open(output_filename, 'w')
# fhandle2 = open(output_filename, 'wb')
# pickle.dump(d, fhandle2)
# fhandle2.write(str(l) + '&' + str(d) + '\n')
# fhandle2.write('Good morning\n')
# fhandle2.write('How are you?\n')
# fhandle2.write('%s\n' % num)
fhandle2.close()

# myfile = open(output_filename, 'r')
# myfile = open(output_filename, 'rb')
# e = pickle.load(myfile)
# print(e)
# df = myfile.readline()
# parts = df.split('&')
# print(parts)
# print(eval(df))
# objects = [eval(l) for l in parts]
# for o in objects:
#     print(type(o))
# print(myfile.readline())
# print(myfile.readline())

# fhandle is just a wrapper, it does not contain the file's contents
# print(fhandle)

# for line in fhandle:
#     line = line.rstrip() # The newline is considered a white space, so it's stripped
#     print(line)

# counter = 0
# for line in fhandle:
#     counter += 1
# print(counter)

# inp = fhandle.read()
# print(len(inp))
# print(inp[:25])

# for line in fhandle:
#     print(type(line))
#     break