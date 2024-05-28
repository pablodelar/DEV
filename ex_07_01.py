filename = '/Users/oihane/Documents/Pablo/Python/sample.txt'

fhandle = open(filename, 'r')

for line in fhandle:
    line = line.rstrip()
    print(line.upper())