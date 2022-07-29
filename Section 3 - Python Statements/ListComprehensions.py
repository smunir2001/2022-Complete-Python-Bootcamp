myString = 'hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)
print()

myList = [letter for letter in myString]
print(myList)
print()

myList = [num for num in range(0, 11)]
print(myList)
print()

myList = [num ** 2 for num in range(0, 11)]
print(myList)
print()

myList = [x ** 2 for x in range(0, 11) if x % 2 == 0]
print(myList)
print()

celsius = [0, 10, 20, 34.5]
print(celsius)
fahrenheit = [(9/5 * temp + 32) for temp in celsius]
print(fahrenheit)
print()

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)
print()

myNewList = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        myNewList.append(x * y)
print(myNewList)
print()

myNewList = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(myNewList)
print()