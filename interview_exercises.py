# Unpacking/starred expressions (*)
def func():
    return [1, 2, 3, 4, 5]

a, *b, c = func()
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

def another_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

result = another_func(*b)
print(result)  # 9

# Shallow vs Deep copy
import copy
# copy() function (Shallow copying) creates a new object and inserts references to the original elements.
# deepcopy() function (Deep copying) creates a new object and recursively inserts copies of the original elements.

print('=' * 100)

# Generators
def count_up():
    count = 1
    while True:
        yield count
        count += 1

counter = count_up()

# a) direct call
# print(counter.__next__())

# b) using next()
# print(next(counter))  # 1
# print(next(counter))  # 2

# c) via a loop
# for gen_result in counter:
#     print(gen_result)


from collections import Counter

my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
counter = Counter(my_list)
most_common_elements = counter.most_common()
print(most_common_elements)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
s = set(my_list)
print(list(s))


my_list = [
    {"name": "Alice", "age": 30}, 
    {"name": "Bob", "age": 25}, 
    {"name": "Charlie", "age": 35}
    ]
sorted_list = sorted(my_list, key=lambda x: x["age"])
print(sorted_list)

print('=' * 100)
print('=' * 100)

# Replace string space with a given character
s = 'l vey u'
# print(s.replace(' ', 'o'))

def str_replace(s, c):
    modified_str = ''
    for i in s:
        if i == ' ': i = c
        modified_str += i
    return modified_str

print(str_replace(s, 'o'))

# Perfect square
import math
def perfect_square(num):
    # square = int(num**0.5)
    # return bool(square**2 == num)
    return (int(math.sqrt(num))**2 == num)

print(perfect_square(10))
print(perfect_square(36))

print('=' * 100)
print('=' * 100)

# Return the number of trailing zeroes in n factorial (n!)
def factorial_for(num):
    f = 1
    for i in range(num, 0, -1):
    # for i in reversed(range(1,8)):
        # print(i)
        f *= i
    return f

def factorial_while(num):
    f = num
    print('factorial: {}'.format(f))
    while num > 1:
        print('num before: {}'.format(num))
        f *= num - 1
        print('factorial en el while: {}'.format(f))
        num -= 1
        print('num after: {}'.format(f))
    return f

# factorial = factorial_for(18)
factorial = factorial_while(18)

def trailing_zeroes(num):
    count = 0
    # for i in reversed(str_num):
    for i in str(num)[::-1]:
        # print(i)
        if i == '0': count += 1
        else: break
    return count

print(trailing_zeroes(factorial))

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# String segmentation
def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        # print(i)
        first_str = s[0:i]
        print('first_str: ', first_str)
        if first_str in dictionary:
            second_str = s[i:]
            print('second_str: ', second_str)
            if (
                not second_str
                or second_str in dictionary
                or can_segment_str(second_str, dictionary)
            ):
                return True
    return False

s = "pepedatacamp"
dictionary = ["data", "camp", "cam", "lack", "pepe"]
print(can_segment_str(s, dictionary))

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# Remove duplicates from a list
l = [1,2,2,3,4,5,5,6,6,7,8,9,9]
d = dict()
new_l = list()
print('List BEFORE: ', l)

for i in l:
    print(i)
    if i not in d:
        d[i] = True
        new_l.append(i)

print(new_l)

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# Find the missing number in the list
def find_missing(input_list):
    sum_of_elements = sum(input_list)
    print(sum_of_elements) # 19
    # There is exactly 1 number missing
    n = len(input_list) + 1
    print(n)
    actual_sum = (n * ( n + 1 ) ) / 2
    print(actual_sum)
    
    return int(actual_sum - sum_of_elements)
list_1 = [1,5,6,3,4]


print(find_missing(list_1))
# 2

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# Lambda
lamb = lambda x,y : x + y
print(lamb(1,2))

# Iterator
l = [1,2,3]
it = iter(l)
for i in it:
    print(i)

# Ternary operator
x = 120
print('YES' if x > 100 else 'NO' if x < 100 else 'EQUAL')