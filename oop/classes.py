# Classes
'''
class myclass:
    var1 = 10
c = myclass()
print(c.var1)

class Employee:
    def __init__(self, name, empid) -> None:
        self.name = name
        self.empid = empid

    def greet(self):
        print('Thanks for joining ABC Company {}!!'.format(self.name))

emp1 = Employee('Pumuki', 12345)
print('Name : ', emp1.name)
print('Employee ID : ', emp1.empid)
emp1.greet()

emp1.name = 'Mofli'
emp1.greet()

# del emp1.empid
print(emp1.empid)

emp2 = Employee('Sander', 23456)
print(emp2.empid)

emp2.country = 'Spain'
print(emp2.country)
'''

############################################ Inheritance ############################################

class person: # Parent Class
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print('Name :- {}'.format(self.name)) 
        print('Age :- {}'.format(self.age)) 
        print('Gender :- {}'.format(self.gender))

class student(person): # Child Class
    def __init__(self, name, age, gender, studentid, fees) -> None:
        super().__init__(name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def studentinfo(self):
        print('Student ID :- {}'.format(self.studentid))
        print('Fees :- {}'.format(self.fees))

class teacher(person): # Child Class
    def __init__(self, name, age, gender, empid, salary) -> None:
        super().__init__(name, age, gender)
        self.empid = empid
        self.salary = salary

    def teacherinfo(self):
        print('Employee ID :- {}'.format(self.empid))
        print('Salary :- {}'.format(self.salary))

stud1 = student('Darko', 45, 'male', 12345, 100)
print('Student Details')
print('---------------')
stud1.personinfo()
stud1.studentinfo()

teacher1 = teacher('Basit' , 36 , 'Male' , 456 , 80000)
print('Employee Details')
print('---------------')
teacher1.personinfo()
teacher1.teacherinfo()

# assert isinstance('john',str)

# Iterator
iterl = ['1','2','3','4','5']
list_iter = iterl.__iter__()
print(type(list_iter))
list_iter2 = iter(iterl)
print(type(list_iter2))

# Generator
def mygen():
    for i in range(1,20):
        yield i
num = list(mygen())
print(num)
gen2 = (i**2 for i in range(10))
print(gen2)

# Decorator -> It is very powerful and useful tool in Python as it allows us to wrap another function in order to extend the behavior of wrapped function without permanently modifying it.
def subtract(num1 , num2):
    res = num1 - num2
    print('Result is :- ', res)

# subtract(4,2)
# subtract(2,4)

def sub_decorator(func):
    def wrapper(num1,num2):
        if num1 < num2:
            num1,num2 = num2,num1
            return func(num1,num2)
    return wrapper

sub = sub_decorator(subtract)
# sub(2,4)

# Decorating a function in one step
@sub_decorator
def subtract2(num1 , num2):
    res = num1 - num2
    print('Result is :- ', res)

subtract2(2,4)
subtract2(4,2)
# Multiple decorators can be applied to the same function.

