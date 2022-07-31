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
print()

# Interactions between Python functions
example = [1, 2, 3, 4, 5, 6, 7]
print(f'example: {example}')
from random import shuffle
shuffle(example)
print(f'shuffle(example): {example}')
print()

# Interactions between Python functions
# myList = ['', 'O', '']
# print(myList)
# shuffle(myList)
# print(myList)

def playerGuess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1, or 2 --> ')
    return int(guess)

def checkGuess(inputList, guess):
    if inputList[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(inputList)
# initial list
myList = ['', 'O', '']
# shuffle list
mixedUpList = shuffle(myList)
# user guess
guess = playerGuess()
# check guess
checkGuess(mixedUpList, guess)
print()