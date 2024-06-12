# Tutorial exercises around files handling
import os

myfile = open('../../sample.txt', 'r')
strfile = myfile.read()
# print(strfile)

strfileend = myfile.read()
print(strfileend) # This won't return any text because the cursor is already at the end of the file

myfile.seek(0) # Seek(0) will move the cursor back to the first character position of the file content

strfileend = myfile.read()
print(strfileend)

myfile.seek(9) # Move the cursor to position 9 in the file content
print(myfile.read())

myfile.seek(0)
print(myfile.read(24)) # Read the first 24 characters of the file

print(myfile.tell()) # Get the file cursor current position

myfile.seek(0)
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

myfile.seek(0)
# print(type(myfile.readlines())) # List of strings (each line of the file)
for line in myfile.readlines():
    # print(type(line)) # String
    print(line)


# Writing files
filetowrite = open('../../sample.txt', 'a') # Open the file in 'append' mode
filetowrite.write('\nTHIS IS THE NEW CONTENT APPENDED IN THE FILE')
filetowrite.close()
filetowrite = open('../../sample.txt')
print(filetowrite.read())

# filetowrite2 = open('../../samplet.txt', 'w') # Open the file in 'write' mode. This will overwrite any previous content in the file
# filetowrite2.write('NEW CONTENT ADDED IN THE FILE. PREVIOUS CONTENT HAS BEEN OVERWRITTEN.')
# filetowrite2.close()
# filetowrite2 = open('../../samplet.txt')
# print(filetowrite2.read())

os.remove('../../samplet.txt')