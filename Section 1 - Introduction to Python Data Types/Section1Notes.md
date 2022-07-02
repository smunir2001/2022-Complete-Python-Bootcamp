smunir2001@gmail.com | July 2, 2022 | Section1Notes.md
# Section 1 - Introduction to Python Data Types
## Files included:
* Numbers.py
* Strings.py

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