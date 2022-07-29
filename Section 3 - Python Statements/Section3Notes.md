smunir2001@gmail.com | July 28, 2022 | Section3Notes.md
# Section 3 - Python Statements
## Files included:
* IfElifElse.py
* ForLoops.py
* WhileLoops.py
* UsefulOperators.py
* ListComprehensions.py
## Control flow
Control flow allows us to only execute certain code when a particular condition as been met.

To control this flow of logic we use some keywords:
* if
* elif
* else

Control flow syntax makes use of colons and indentation (whitespace).
This indentation system is crucial to Python and is what sets it apart from other programming languages.
* Syntax of an __if__ statement
```Python
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else
```
## For loops
Many objects in Python are "iterable", meaning we can iterate over every element in the object.

Such as every element in a list or every character in a string.

We can use for loops to execute a block of code for every iteration.
```Python
my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)
```
## While loops
While loops will continue to execute a block of code while some condition remains True.
```Python
while some_boolean_condition:
    # do something
else:
    # do something different
```
__break, continue, pass__
We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:
* __break:__ breaks out of the current closest enclosing loop.
* __continue:__ goes to the top of the closest enclosing loop.
* __pass:__ does nothing to all.
## Useful operators
```Python
myList = [1, 2, 3]
for num in range(10):
    # generature numbers 0 - 10 (0 inclusive, 10 exclusive)
    print(num)
```
## List comprehensions
List comprehensions are a unique way of quickly creating a list with Python.

If you find yourself using a for loop along with .append() to create a list, List comprehensions are a good alternative!