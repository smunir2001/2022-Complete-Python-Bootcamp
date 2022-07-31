smunir2001@gmail.com | July 30, 2022 | Section4Notes.md
# Section 4 - Methods & Functions
## Files included:
* Methods.py
* Functions.py
* TupleUnpacking.py
## Python documentation
[Python 3.6.4 Documentation](https://docs.python.org/3/)
```Python
myList = [1, 2, 3]
myList.append(4)
print(myList)

myList.pop()
print(myList)
```
## Introduction to functions
Creating clean repeatable code is a key part of becoming an effective programmer.

__Functions__ allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code.

Functions will be a huge leap forward in your capabilities as a Python programmer.

This means that the problems you are able to solve can also be a lot harder!
## __Def__ keyword & functions
Creating a function requires a very specific syntax, inncluding the __def__ keyword, correct indentation, and proper structure.
```Python
def name_of_function():
    '''
    Docstring explains function.
    '''
    print('Hello world')
```
Typically we use the __return__ keyword to send back the result of the function, instead of just printing it out.

__Return__ allows us to assign the output of the function to a new variable.
## Tuple unpacking with Python functions
* Return multiple items from a function with tuple unpacking.
* We can loop through a list of tuples and unpack the values within them.
## __*args__ and __**kwargs__ in Python
Functional parameters...
* arguments
* keyword arguments
## Lambda expressions, Map, and Filter functions
