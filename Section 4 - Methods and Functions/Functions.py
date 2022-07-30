def helloWorld():
    '''my first Python function'''
    print('running function helloWorld()...')
    print('Hello world!')
helloWorld()

def helloWorld(name):
    print('\nrunning function helloWorld(name)...')
    print('Hello', name)
helloWorld('Sami')

def addTwoNumbers(num1, num2):
    return num1 + num2
print('\nrunning function addTwoNumbers(num1, num2)...')
print('addTwoNumbers(2, 3) = ', addTwoNumbers(2, 3))
