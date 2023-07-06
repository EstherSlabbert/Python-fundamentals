import struct
import datetime as dt
import sys

"""
For additional practice questions/exercises:
https://pythonlobby.com/python-function-exercises-with-solution/
https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
https://www.w3resource.com/python-exercises/python-basic-exercises.php
https://automatetheboringstuff.com
"""

"""
Question 1 - Closest to Zero

Implement closest_to_zero function to return the integer in the array ints that is closest to zero.
If there are two integers equally close to zero, consider the positive element to be closer to zero 
(example: if ints contains -5 and 5, return 5).If ints is None or empty, return 0.
Input: integers in ints have values ranging from -2147483647 to 2147483647.
eg. ints = [55, 77, 33, 3, -3, -4, 4] should return 3
"""


def closest_to_zero(ints):
    # checks if the input list ints is empty or None to return 0
    if not ints:
        return 0

    # starting point at 1st item in array
    closest = ints[0]
    # loops through the list of ints
    for i in range(1, len(ints)):
        # checks if int in array is closer to 0 than 1st int
        if abs(ints[i]) < abs(closest):
            # updates closest to be the int closer to 0
            closest = ints[i]
        # checks if int has a positive counterpart equidistant from 0
        elif abs(ints[i]) == abs(closest) and closest < 0:
            # updates closest to be the positive option
            closest = ints[i]
    # returns number closest to 0 (positive one if 2 no.s equidistant)
    return closest


"""
Question 2 - Sort Sentence By Word Length

Given any string your code should return a List of words in Ascending order by the length of the word.
For example, running the function sort_by_length_of_words() :
sort_by_length_of_words ("here is a block of text with differing sized words")
Should return:
[a, is, of, here, text, with, block, sized, words, differing]
"""


def ascending_order_word_length(string_of_words):
    string_of_words = string_of_words.split()
    return sorted(string_of_words, key=len, reverse=False)


"""
Question 3 - find largest number

Given an array of numbers called numbers the function should find and return the largest number.
The array numbers always contains at least one number.
find_largest(numbers) should return the largest number from numbers.
e.g. numbers = [900, 80, 5 -988, -98, 36666, 75755, 987, 8, 0] should return 75755
Implement find_largest(numbers).
"""


def find_largest(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest


"""
Question 4 - Twin words

A twin of a word is a word written with the same letters (case insensitive) but not necessarily in the same order.
For example Silent is a twin of Listen.
The is_twin(a, b) function should return True if b is the twin of a and False otherwise.
a and b are two strings and are not None.
Write the body of the is_twin(a, b) function.
"""


def is_twin(a, b):
    a = sorted(list(a.lower()))
    b = sorted(list(b.lower()))
    if a == b:
        return True
    else:
        return False


"""
Question 5 - Evaluate Password Length

In a function, create a control flow (if statement) that will evaluate a string for its size and output the below messages:
< 5 in length must return the string: "Your password is too short."
20 in length, the method must return: "Your password is too long and may be forgotten."
In between 5-20 the method must return: "Your password is an acceptable length."
"""


def control_flow(password):
    if len(password) < 5:
        return "Your password is too short"
    elif len(password) > 20:
        return "Your password is too long and may be forgotten"
    else:
        return "Your password is an acceptable length"


# Showing results of functions

# provides a list of integers called int
ints = [55, 77, 33, 3, -3, -4, 4]
# the closest_to_zero function returns the number closest to 0 (+ number if numbers are equidistant from 0)
print(closest_to_zero(ints))
# expect: 3

# the ascending_order_word_length returns a list of words from the sentence in ascending order of length
print(ascending_order_word_length("This is a string of words that I have written"))
# expect: [a, is, of, here, text, with, block, sized, words, differing]

# provides a list of integers called numbers
numbers = [900, 80, 5 -988, -98, 36666, 75755, 987, 8, 0]
# the find_largest function finds the largest number in a list of numbers and returns it
print(find_largest(numbers))
# expect: 75755

# is_twin function returns whether the words have the same letters or not
print(is_twin("word", "dwor"))
# expect True

print(is_twin("happy", "unhappy"))
# expect False

# input asks user to input a password and control_flow function returns a sentence about the length of the password
print(control_flow(input("Enter a password: ")))
# expect result according to input

# Testing string slicing and passing with different version of concatenation

string = "Hello World!"
print(string[-4:-7:-1])
# expect roW

# gives date from an array format
exam_st_date = (11, 12, 2014)
# returns date in a different format by referencing the array
print("The examination will start from : %i / %i / %i"%exam_st_date)
# expect The examination will start from : 11 / 12 / 2014

# Testing out imported libraries:

# returns Python version and when it was installed
print(f"Python version: {sys.version}")

# returns current date and time
print(dt.datetime.now())

# returns the purpose of the built-in function 'abs'
print(abs.__doc__)
# expect Return the absolute value of the argument.

# used to calculate the size of a pointer (in this case P) in bytes and then multiply it by 8 to get the size in bits
# 32-bit system, a pointer requires 4 bytes, and on a 64-bit system, a pointer requires 8 bytes
print(struct.calcsize("P") * 8)
# expect 64
