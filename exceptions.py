import sys

try:
    print(100/0)
except:
    print(sys.exc_info()[1], 'Exception occurred')
else:
    print('No exception occured')
finally:
    print('Run this block of code always')
