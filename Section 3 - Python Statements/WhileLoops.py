x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')
print()

x = [1, 2, 3]
for item in x:
    # comment
    pass
print('end of my script.')
print()

myString = 'Sami'
for letter in myString:
    if letter == 'a':
        continue
    print(letter)
print()

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print()