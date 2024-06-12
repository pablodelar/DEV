# str = 'X-DSPAM-Confidence: 0.8475  '

# start = str.find(':')
# fl = float(str[start + 1:].strip()) # We don't need to use strip() before converting to float, since float function will ignore whitespaces.
# print(type(fl))

# Convert binary digits to integer with ord
b = '1101'
i = 0
while b != '':
    i = i * 2 + (ord(b[0]) - ord('0'))
    b = b[1:]

print('==========> ', i)