def helloWorld():
    '''my first Python function'''
    print('running function helloWorld()...')
    print('Hello world!')
helloWorld()

def helloWorld(name):
    print('\nrunning function helloWorld(name)...')
    print(f'Hello {name}!')
helloWorld('Sami')

def addTwoNumbers(num1, num2):
    return num1 + num2
print('\nrunning function addTwoNumbers(num1, num2)...')
print('addTwoNumbers(2, 3) = ', addTwoNumbers(2, 3))

def sayHello(name = 'Default'):
    print('\nrunning function sayHello(name)...')
    print(f'Hello {name}!')
sayHello()

def checkEvenNumber(number):
    return number % 2 == 0
print('\nrunning function checkEvenNumber(number)...')
print('checkEvenNumber(20) =', checkEvenNumber(20))

def checkEvenList(numList):
    for number in numList:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
print('\nrunning function checkEvenList(numList)...')
print('checkEvenList([1, 3, 5]) =', checkEvenList([1, 3, 5]))
print('checkEvenList([2, 4, 5]) =', checkEvenList([2, 4, 5]))