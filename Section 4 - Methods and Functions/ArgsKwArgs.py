def myFunc(a, b):
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05

def myFunc2(a, b, c = 0, d = 10):
    return sum((a, b, c, d)) * 0.05

def myFunc3(*args):
    # *args is a tuple of parameters/arguments
    return sum(args) * 0.05

def myFunc4(*spam):
    print(spam)

def myFuncA(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here.')
myFuncA(fruit = 'apple', veggie = 'lettuce')

def myFuncB(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I woud like {} {}'.format(args[0], kwargs['food']))
myFuncB(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dog')