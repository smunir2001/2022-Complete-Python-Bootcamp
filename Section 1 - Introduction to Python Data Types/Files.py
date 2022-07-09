# smunir2001@gmail.com | July 8, 2022 | Files.py

myFile = open('myFile.txt')
print('1. Contents of myFile.txt:')
print(myFile.read())
myFile.seek(0) # resets the cursor...
print('\n2. Contents of myFile.txt:')
print(myFile.read())
myFile.seek(0) # resets the cursor...
print('\n2. Contents of myFile.txt using readlines()')
print(myFile.readlines())
myFile.close()

with open('myFile.txt') as my_new_file:
    contents = my_new_file.read()
    print('\n3. Contents of myFile.txt:')
    print(contents)
    my_new_file.close()

with open('myNewFile.txt', mode = 'r') as f:
    print('\n4. Contents of myNewFile.txt:')
    print(f.read())
    f.close()

with open('myNewFile.txt', mode = 'a') as f:
    f.write('\nFOUR ON FOURTH')
    f.close()

with open('myNewFile.txt', mode = 'r') as f:
    print('\n4. Contents of myNewFile.txt after append...:')
    print(f.read())
    f.close()

with open('blah.txt', mode = 'w') as f:
    f.write('I created this file!')
    f.close()

with open('blah.txt', mode = 'r') as f:
    print('\n5. Contents of new file (blah.txt):')
    print(f.read())
    f.close()