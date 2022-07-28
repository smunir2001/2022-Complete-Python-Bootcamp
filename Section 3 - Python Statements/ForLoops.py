print('lists & for loops')
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in myList:
    print(num)
print()

for item in myList:
    print('Item ', item)
print()

for number in myList:
    # check for even number
    if number % 2 == 0:
        print('\t', number, 'is even.')
    else:
        print(number, 'is ODD.')
print()

listSum = 0
for values in myList:
    listSum += values
print('listSum = ', listSum)
print()

myString = 'Hello Sambreezy'
for letter in myString:
    print(letter)
print()

# for _ in myString:
    # print('Zzz')
# print()

print('tuples & for loops')
tup = (1, 2, 3)
for item in tup:
    print(item)
print()

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print('my_list = ', my_list)
print('len(my_list) = ', len(my_list))
for item in my_list:
    print(item)
print()

for (a, b) in my_list:
    print('|', a, '|', b, '|')
print()

myList2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for (a, b, c) in myList2:
    print('|', a, '|', b, '|', c, '|')
print()

myDict = {'k1' : 1, 'k2' : 2, 'k3' : 3}
# print('myDict = ', myDict)
for item in myDict:
    print(item)
print()
for elem in myDict.items():
    print(elem)
print()

for key, value in myDict.items():
    print(value)
print()