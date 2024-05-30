# print(min("Hello world"))

# print("a", "b", "c",)

b = False
a = True

smallest = None

# print(0 == 0.0)
# print(0 is 0.0) # is demands equality in both data type and value

# Try to only use the 'is/is not' operators on Booleans and None comparisons.


total = 0
count = 0
while True :
    x = input('> ')
    if x == 'done' :
        break
    try :
        ival = int(x)
    except :
        print('Invalid input')
        continue
    count += 1
    total += ival
if count == 0 :
    print('Total = 0, Count = 0, Average = 0')
else :
    print(f'Total: {total}, Count: {count}, Average: {total / count}')