from functools import reduce

str = 'X-DSPAM-Confidence: 0.8475  '

start = str.find(':')
fl = float(str[start + 1:].strip()) # We don't need to use strip() before converting to float, since float function will ignore whitespaces.
print(type(fl))

# Convert binary digits to integer with ord
b = '1101'
i = 0
while b != '':
    i = i * 2 + (ord(b[0]) - ord('0'))
    b = b[1:]

# print('==========> ', i)

# Or use the built-in functions
int('1101',2) # 13
bin(13) # 1101


mylist= ['one','two','three','four','one','two','two','three','five','five','six','seven','six','seven','one','one','one','ten','eight','ten','nine','eleven','ten','ten','nine']
d = dict()
for word in mylist:
    d[word] = d.get(word, 0) + 1

# print(d)

a = 5
b = 2
x = 'Asif'
y = 'Bhat'

# Division(floor)
c = a // b
print('Floor division of {} by {} will give :- {}\n'.format(a,b,c))

# Testing function documentation string
def testfunction(num):
    '''Function that prints whether a number is even or odd'''
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
print(testfunction.__doc__)

country = 'Chile'
def funk(city = 'Santiago'):
    print('Capital of {}: '.format(country), city)
funk()


list1 = [11,22,33,44,55]
print(id(list1))
def myfunc(list1):
    print(id(list1))
    list1 = [10,100,1000,10000]
    print(id(list1))

print('"List1" before calling the function:- ',list1)
myfunc(list1)
print('"List1" after calling the function:- ',list1)

print('\n' + ('*' * 100) + '\n')

def add(*args):
    # print(type(args)) # Tuple
    return sum(args)
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,3,4,5))

l = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,5,6,7]
t = (1,2,3,4,5,6,7)
# print(add(*l)), print(add(*t))
# print(add(*l, *l2))

def userdetails(**kwargs):
    # print(type(kwargs)) # Dict
    for key,val in kwargs.items():
        print('{} : {}'.format(key, val))
# kargstype = userdetails(Name = 'Asif' , ID = 7412 , Pincode = 41102 , Age = 33 , Country = 'India', Language = 'Hindi')
# print(type(kargstype))

mydict = {'a' : 1, 'b' : 2, 'c' : 3}
userdetails(**mydict)

print('\n' + ('*' * 100) + '\n')

def UserDetails(licenseNo, *args , phoneNo=0 , **kwargs): # Using all four argum
    print('License No :- ', licenseNo)
    j=''
    for i in args:
        j = j+i
    print('Full Name :-',j)
    print('Phone Number:- ',phoneNo)
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))


name = ['Asif' , ' ' , 'Ali' , ' ','Bhat']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India', 'Language': 'Hindi'}
UserDetails('BHT145' , *name , phoneNo=1234567890,**mydict )


############################################ Lambda, Filter, Map and Reduce ############################################

print('*' * 100 + '\n' + ('*' * 100) + '\n')

# Lambda
addition = lambda a, b : a + b
print(addition(5, 10))

def myfunc(n):
    return lambda a : a + n
add10 = myfunc(10)
print(add10(5))

# Filter
list1 = [1,2,3,4,5,6,7,8,9]
odds = list(filter(lambda n : n%2 == 1, list1))
print(odds)

def oddf(n):
    if n%2 == 1 : return True
    else: return False
oddl = list(filter(oddf, list1))
print(oddl)

# Map
def twice(n):
    return n*2
doubles = list(map(twice, oddl))
print(doubles)

doubles2 = list(map(lambda n: n*2, oddl))
print(doubles2)

# Reduce
def add(a,b):
    return a+b
sum_all = reduce(add, doubles)
print(sum_all)
sum_all2 = reduce(lambda a,b : a+b, doubles)
print(sum_all2)

# All together
sum_all3 = reduce(lambda a,b : a+b, list(map(lambda n : n*2, list(filter(lambda n : n%2==1, list1)))))
print(sum_all3)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list(map(lambda x, y: x + y, list1, list2)))

print(reduce(lambda a,b: bool(a and b), [0, 0, 1, 0, 0]))

# Dictionary Comprehension
d = {i:1+7 for i in range(1, 10)}
print(d)


# Send an email using Python
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("pythonexercises@pabs.com", "123456")
message = "Hola"
s.sendmail("pythonexercises@pabs.com", "pablo.delar@gmail.com", message)


# Decorator exercise
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()