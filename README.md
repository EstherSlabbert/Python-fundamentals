# Python Fundamentals

- [Python Fundamentals](#python-fundamentals)
  - [Variables](#variables)
  - [Operators](#operators)
  - [Control flow](#control-flow)
  - [Strings - "str"](#strings---str)
    - [Indexing](#indexing)
    - [Slicing](#slicing)
    - [Concatenation \& Casting](#concatenation--casting)
  - [Numbers - "float", "int"](#numbers---float-int)
  - [Booleans - "bool"](#booleans---bool)
  - [Lists - "list"](#lists---list)
  - [Dictionaries - "dict"](#dictionaries---dict)
  - [Functions](#functions)
  - [Libraries and modules](#libraries-and-modules)

## Variables

Variables are references to store some data (containers for storing data values).

```python
my_variable = "some data"
```

There are several data types. They include:

- Strings (characters between `""` or `''`)
- Numbers
  - Integers = whole numbers (positive or negative) eg. `4, -1, 0`
  - Floats = Floating point number (decimals) eg. `3.14, 0.1, -9.432`
  - Complex numbers = Huge numbers, that can only be derived by a formula.
- Booleans (`True` or `False`)
- Collections
  - Lists (Arrays) = mutable `["item", 1, True]`
  - Dictionaries (work using key-value pairs) `{key: value}` (key = reference to an object; value = data stored in said object)
  - Tuples = immutable `("item", 1, True)` (memory efficient) accessed using indexes`tuple[0]`
  - Sets (unordered list, can be changed, have no index, prints out randomly eg. `car_parts = {"wheels", "doors", "windows"}` can .add() and .discard())
  - Frozen Sets (cannot be changed, but is unordered eg. `x = frozenset([1, 2, 3, 4])`)
- None = defines null objects and variables & is not 0 or any other value. (Note: Use 'is None' or 'is not None' to do an identity comparison) `x = None`

To determine data type `type(data)`.

## Operators

| Arithmetic operators                                                | Comparison operators          |
|---------------------------------------------------------------------|-------------------------------|
| "+" Addition                                                        | "==" equal to                 |
| "-" Subtraction                                                     | "!=" not equal to             |
| "*" Multiplication                                                  | ">" greater than              |
| "/" Division                                                        | "<" less than                 |
| "%" Modulo (finds remainder when one integer is divided by another) | ">=" equal to or greater than |
| "**" Exponent                                                       | "<=" equal to or less than    |

## Control flow

Allows you to make decisions in your code.

- `if`,`elif`,`else`: Conditional statements.
- `for _ in ____:`: Looping iterable objects. Often used to iterate through embedded lists.
- `while _______:`: Looping continues as long as condition `True`. May use incrementer to break out(`x += 1`). Often used to verify user input.
- `break`: Exits loop prematurely.
- `continue`: Used to skip next iteration in loop.
- `quit()`&`exit()`: Ends a program/ exits.

## Strings - "str"

```python
escape_example = "I said \"Wow!\""
reverse_quote_in_quote = "I said 'Wow!'"
```

### Indexing

| characters     | H   | e   | l   | l  | o  |    | w  | o  | r  | l  | d  | !  |
|----------------|-----|-----|-----|----|----|----|----|----|----|----|----|----|
| index          | 0   | 1   | 2   | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 |
| negative index | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

### Slicing

```python
hi = "Hello World!"
print(hi[-4:-7:-1]) # returns 'roW' - str[start:end+1:step]
```

| Methods            | Usage                                               |
|--------------------|-----------------------------------------------------|
| .strip()           | Gets rid of whitespaces at the end, not inbetween.  |
| len(str)           | Gives the length of the string.                     |
| .upper()           | Makes everything uppercase.                         |
| .lower()           | Makes everything lowercase.                         |
| .split()           | Splits into substrings based on delimiter provided. |
| .capitalize()      | Capitalizes the first letter in a string.           |
| .replace("a", "b") | Replaces each "a" in string with "b".               |

### Concatenation & Casting

```python
hi = "Hello"
name = "John Smith"
age = 26
# concatenation
print(hi + ", "  + name + " who is age " + str(age) + ".") # Hello, John Smith who is age 26.
# f-string
print(f"{hi}, {name} who is age {age}.") # Hello, John Smith who is age 26.
```

Casting (sets type): float(), bool(), int(), str(). Used as different types cannot interact (usually in concatenation).

## Numbers - "float", "int"

```python
pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}") # 3.142 round to a specific number of decimals
score = 18
maximum = 30
print(f"You scored {score/maximum}") # get decimal 0.6
print(f"You scored {score/maximum:%}") # get % 60.000000%
print(f"You scored {score/maximum:.2%}") # get % and round to 2 decimals 60.00%
```

## Booleans - "bool"

- Any string is True except empty strings.
- Any number is True except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

```python
a = True
b = False
print(a == b) # False
print(a != b) # True
print(a >= True) # True
print(b <= False) # True
hi = "Hello World!"
print(hi.isalpha()) # False
print(hi.islower()) # False
print(hi.endswith("!")) # True
print(hi.startswith("H")) # True
```

## Lists - "list"

| Methods                      | Usage                                                                                                                |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|
| len(list)                    | Counts number of items in list.                                                                                      |
| .append(item)                | Adds item to the end of the list.                                                                                    |
| .extend(list2)               | Extends list by adding items from another list.                                                                      |
| .pop(index)                  | Removes item from list.                                                                                              |
| .index(item)                 | Returns index of item.                                                                                               |
| .insert(index, item)         | Inserts item into list at a specified index.                                                                         |
| .remove(item)                | Removes first instance of item from list.                                                                            |
| .sort(reverse=True, key=len) | Sorts list in descending order by length of items in alphabetical order. Default is ascending and alphabetical only. |
| .reverse() /`list[::-1]`     | Reverses current order of list.                                                                                      |
| .clear()                     | Clears the list.                                                                                                     |
| `list[0] = "new_item"`       | Replaces 1st item in list with new_item.                                                                             |
| `list[2::3]`                 | Returns 3rd item in list & every 3 items from the 3rd [start:end+1:step]                                             |
| `max(list)` `min(list)`      | Returns maximum number & minimum number respectively in list.                                                        |
| `sum(list)`                  | Returns sum of all numbers in a list.                                                                                |

## Dictionaries - "dict"

| Method                    | Usage                                                 |
|---------------------------|-------------------------------------------------------|
| .keys()                   | Returns `dict_keys([list keys])`.                     |
| .values()                 | Returns `dict_values([list values])`.                 |
| .items()                  | Returns `dict_items([(tuple key-value pairs)])`.      |
| `dict[key].remove(value)` | Removes a specific value from a list stored in a key. |
| `dict[key]`/`.get(key)`   | Returns the corresponding value.                      |

```python
dict1 = {"name": "esther",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"]}
list_of_values = []
# print list of values without brackets
for item in dict1.keys():
    list_of_values.append(dict1[item])
    print(*list_of_values, sep = ", ") # esther, DevOps, 3, ['variables', 'data_types']
```

## Functions

Functions allow us to not duplicate code! (make reusable code). They also make code cleaner and easier to read.
DRY - Don't Repeat Yourself

- define your functions at the start of doc
- each function should do one thing (can do more later when more confident)
- name them properly (tell us what it does)
- Use comments to explain function purpose - Comments showcase what they do

```python
# function to return multiple arguments
def my_function(*multiargs): # * allows for any number of arguments
    return multiargs # returns tuple
```

(See [fizz_buzz program](https://github.com/EstherSlabbert/Python-fundamentals/blob/main/fizz_buzz_v2.py) or [movie_rating program](https://github.com/EstherSlabbert/Python-fundamentals/blob/main/movie_ratingz_v2.py))

## Libraries and modules

A library is a collection of related modules or packages.
A module is a set of code/functions with the .py extension that can be called in a separate .py file.

```python
from random import * # imports everything from random library
import os, datetime, sys, math, subprocess
import requests
num_float = 23.66
print(math.ceil(num_float)) # 24 # rounds up
print(math.floor(num_float)) # 23 # rounds down
print(math.pi) # 3.14159...
print(sys.version) # version of Python you are using
working_dir = os.getcwd() # current location of file
os.chdir("C:/Users/super/Documents/") # changes directory
os.mkdir("C:/Users/super/Documents/test_dir1") # makes a new directory
subprocess.run(["python", "hello_world.py"]) # language/file type, file name
print(datetime.date.today()) # today's date #.now() gives time down to sec
request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code) # 200
print(request_bbc.content) # source code for bbc website
```

JSON - JavaScript Object Notation, great way to transfer data between systems (XML is alternative). A standardized format commonly used to transfer data as text that can be sent over a network.

Every script is a program. Not every program is a script.
