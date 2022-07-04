# smunir2001@gmail.com | July 2, 2022 | Strings.py

print('Hello...')
print('world')
print('Hello world!')
print("I'm going on a run yay!")
print("Hello\n world");
print("lol that was so weird...")
print("number of characters: ", len("helloWorld"))
print()
myString = 'Hello world'
print("myString = ", myString)
print("myString[0] = ", myString[0])
print("myString[9] = ", myString[9])
# reverse-indexing
print("myString[-2] = ", myString[-2])

myString = 'abcdefghijk'
print("\nnow myString = ", myString)
print("myString[2:] = ", myString[2:])
print("myString[:3] = ", myString[:3]) # up to but not including
print("myString[3:6] = ", myString[3:6])
print("myString[::] = ", myString[::])
print("myString[::2] = ", myString[::2])
print("myString[::3] = ", myString[::3])
print("myString[::-1] = ", myString[::-1]) # reverse a string

name = "Sam"
print("\nname = ", name)
last_letters = name[1:]
print("last_letters = ", last_letters)
newName = 'P' + last_letters
print("newName = ", newName)
letter = 'z'
print("\nletter = ", letter)
print("letter * 10 = ", letter * 10)

x = 'Hello World'
print('\nx = ', x)
print('x.upper() = ', x.upper())
print('x.lower() = ', x.lower())
print('x.split() = ', x.split())
x = 'Hi this is a string.'
print('\nnow x = ', x)
print('x.split("i") = ', x.split('i'))

my_name = 'Sami'
print('\nHello ' + my_name)

print('This is a string {}'.format('INSERTED'))
print('\nThe {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f = 'fox', b = 'brown', q = 'quick'))

result = 100/777
print('\nresult = ', result)
print('result = {r:1.3f}'.format(r = result))
name = 'Jose'
print(f'Hello, his name is {name}')