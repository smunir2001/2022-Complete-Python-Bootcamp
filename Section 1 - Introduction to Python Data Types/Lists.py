# smunir2001@gmail.com | July 3, 2022 | Lists.py

my_list = [1, 2, 3]
my_list = ['STRING', 100, 23.2]
print('my_list', my_list)
print(len(my_list))
my_list = ['one', 'two', 'three']
another_list = ['four', 'five']
new_list = my_list + another_list
print(new_list)
new_list[0] = 'ONE'
print(new_list)
new_list.append('SIX')
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)

letter_list = ['a', 'e', 'x', 'b', 'c']
print(letter_list)
letter_list.sort()
print(letter_list)
num_list = [4, 1, 8, 3]
print(num_list)
num_list.sort()
print(num_list)