smunir2001@gmail.com | July 2, 2022 | Section1Notes.md
# Section 1 - Introduction to Python Data Types
## Files included:
* Numbers.py
* Strings.py
* Tuples.py
* Sets.py
* myNewFile.txt
* myFile.txt
* Lists.py
* Files.py
* Dictionaries.py
* blah.txt

| Name | Type | Description |
|------|------|-------------|
| Integers | int | Whole numbers, such as: 3 300 200
| Floating point | float | Numbers with a decimal point: 2.3 4.6 100.0 |
| Strings | str | Ordered sequence of characters: "hello" 'Sammy' "2000" |
| Lists | list | Ordered sequence of objects: [10, "hello", 200.3] |
| Dictionaries | dict | Unordered Key:Value pairs: {"mykey":"value", "name":"Frankie"} |
| Tuples | tup | Ordered immutable sequence of objects: (10, "hello", 200.3) |
| Sets | set | Unordered collection of unique objects: {"a", "b"} |
| Booleans | bool | Logical value indicating True or False
## Rules for Variable Names
* Names cannot start with a number.
* There can be no spaces in the name, use _ instead.
* Can't use any of these symbols: '",<>/?|\()!@#$%^&*~-+
* Names should be lowercased.
## Python uses Dynamic Typing
This means you can reassign variables to different data types.

This makes Python very flexible in assigning data types, this is different than other languages that are Statically Typed.
* Pros of Dynamic Typing
    * Very easy to work with.
    * Faster development time.
* Cons of Dynamic Typing
    * May result in bugs for unexpected data types!
    * You need to be aware of __type()__
## Strings in Python
Strings are sequences of characters, using the syntax of either single quotes or double quotes... examples:
* 'hello'
* "Hello"
* "I don't do that"
Because strings are __ordered sequences__ it means we can use indexing and slicing to grab sub-sections of the string.

Indexing notation uses [] notation after the string (or variable assigned to the string).

Indexing allows you to grab a single character from the string.

These actions use [] square brackets and a number index to indicate positions of what you wish to grab.

    Character: h e l l o

    Index: 0 1 2 3 4

    Reverse Index: 0 -4 -3 -2 -1
Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.

This has the following syntax:
    
    [start:stop:step]
start is a numerical index for the slice start.

stop is the index you will go up to (but not include)

step is the size of the "jump" you take.
## Lists in Python
Lists are __ordered sequences__ that can hold a __variety__ of object types.

They use [] brackets and commas to separate objects in the list.
* [1, 2, 3, 4, 5]

Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.
## Dictionaries in Python
Dictionaries are __unordered mappings__ for storing objects. Previously we saw how lists store objects in an ordered-sequence, dictionaries use a __key-value pairing__ instead.

This key-value pair allows users to quickly grab objects without needing to know an index location.
## Tuples in Python
Tuples are very similar to lists. However, they have one key difference: immutability.

Once an element is inside a tuple, it cannot be reassigned.

Tuples use parenthesis: (1, 2, 3)
## Sets in Python
Sets are __unordered collections__ of __unique__ elements.

Meaning there can only be one representative of the same object.
## Booleans in Python
Booleans are operators that allow you to convey True or False statements.

These are very important later on when we deal with control flow and logic!

## I/O with Basic Files in Python
```Python
myFile = open('myFile.txt')
```
Reading, Writing, Appending Modes
* mode = 'r' is read only
* mode = 'w' is write only (will overwrite files or create new)
* mode = 'r+' is reading & writing
* mode = 'w+' is writing & reading (overwrites existing files or creates a new file)