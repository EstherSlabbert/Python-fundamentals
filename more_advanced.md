# Some More Advanced Python

- [Some More Advanced Python](#some-more-advanced-python)
  - [Operators](#operators)
  - [Functions](#functions)
    - [Enumerate](#enumerate)
    - [Bin](#bin)
    - [Chr](#chr)
    - [Ord](#ord)

## Operators

|Operator|Function                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
|  `//`  | Floor division rounds the result of division down to the nearest whole number.              |
|  `//=` | Performs floor division and equates to the new value. `x =// y` is the same as `x = x // y`.|

## Functions

### Enumerate

The `enumerate()` function in Python is used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of each item. It returns an iterator that generates pairs of index-value tuples.

General syntax: `enumerate(sequence, start=0)`, where the `sequence` parameter is the sequence that you want to iterate over, and `start` is an optional parameter that specifies the starting index. By default, the starting index is 0.

For example:

```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(index, fruit)
# returns an iterator that generates pairs of index-value tuples
# returns:
"""
0 apple
1 banana
2 orange
"""
```

`enumerate()` is commonly used when you need to iterate over a sequence and also need access to the index of each item. It simplifies the code by eliminating the need to manually manage an index variable.

### Bin

`bin()` is a function that returns binary representation of numbers.

General syntax: `bin(number)` where `number` is any integer.

For example:

```python
print(bin(1234))
# returns: 10011010010
```

### Chr

The `chr()` function returns the character that represents the specified unicode.

General syntax: `chr(number)` where `number` is any integer representing a valid Unicode code point.

For example:

```python
print("From " + chr(97) + " to " + chr(122))
# returns: From a to z
```

### Ord

The `ord()` function returns the number representing the unicode code of a specified character.

General syntax: `ord(character)` where `character` is any character as a string which can be represented as a valid Unicode code point.

For example:

```python
print("From " + str(ord("a")) + " to " + str(ord("z")))
# returns: From 97 to 122
```
