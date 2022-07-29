myList = [1, 2, 3]
for num in range(10):
    print(num)
print()

for num in range(3, 10):
    print(num)
print()

for num in range(0, 11, 2):
    print(num)
print()

print(list(range(0, 11, 2)))
print()

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
print()

word = 'abcde'
for item in enumerate(word):
    print(item)
print()

myList1 = [1, 2, 3, 4, 5, 6, 7]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]
zip(myList1, myList2)
for item in zip(myList1, myList2):
    print(item)
print()

print(list(zip(myList1, myList2, myList3)))
print()

print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print()

print('a' in 'a world')
print()
print('myKey' in {'myKey' : 345})
print()

myDict = {'myKey' : 345}
print(345 in myDict.values())
print(345 in myDict.items())
print()

myUOList = [10, 20, 30, 40, 100]
print(min(myUOList))
print(max(myUOList))

from random import shuffle
shuffledList = shuffle(myUOList)
print(shuffledList)
print()

from random import randint
print(randint(0, 100))
print()

result = input('Enter a number here: ')
print('You entered ', result)
print(type(result))
print(float(result))
print()