str = 'X-DSPAM-Confidence: 0.8475  '

start = str.find(':')
fl = float(str[start + 1:].strip()) # We don't need to use strip() before converting to float, since float function will ignore whitespaces.
print(type(fl))
