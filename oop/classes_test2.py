class test:
    y = 2
    def __init__(self) -> None:
        self.x = 1
        print('Constructing a new test object...')

myclass = test()
print('y is: {}'.format(myclass.y))
print('x is: {}'.format(myclass.x))

myclass.y = 3
myclass.x = 2

print('y is: {}'.format(myclass.y))
print('x is: {}'.format(myclass.x))

print(test.y)