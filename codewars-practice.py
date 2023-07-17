"""
1. Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    result = []
    list = sentence.split()
    for word in list:
        if len(word) < 5:
            word = word
            result.append(word)
        else:
            word = word[::-1]
            result.append(word)
    return " ".join(result)

# print(spin_words("Hey fellow warriors"))
# expect: Hey wollef sroirraw

"""
# Tests
import codewars_test as test
from solution import spin_words

@test.describe("Stop gninnipS My sdroW!")
def fixed_tests():
    @test.it("Single word")
    def _():
        test.assert_equals(spin_words("Welcome"), "emocleW")
        test.assert_equals(spin_words("to"), "to")
        test.assert_equals(spin_words("CodeWars"), "sraWedoC")

    @test.it("Multiple words")
    def _():
        test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
"""

"""
2. A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcissistic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic
number in base 10.
This may be True and False in your language, e.g. PHP.
Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be
passed into the function.
"""
def narcissistic( value ):
    number1 = value
    number2 = value
    i = 0
    j = 0
    while number1 > 0:
        # the floor division // rounds the result down to the nearest whole number
        number1 //= 10
        i += 1
    while number2 > 0:
        # modulus % gives remainder of num/num eg. 13%5=3
        x = number2 % 10
        number2 //= 10
        j += x ** i
    if j == value:
        return True
    else:
        return False


'''
Alternate solution:
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
'''

# print(narcissistic(153))
# expect: True

"""
# Test
from solution import narcissistic
import codewars_test as test

import random

@test.describe("Submission tests")
def submission_tests():
    
    def dotest(input, expected):
        test.assert_equals(narcissistic(input), expected, f"Incorrect answer for value={input}\n");
        
    
    @test.it("Narcissistic numbers")
    def narcissistic_tests():
        dotest(  7, True)
        dotest(371, True)

    @test.it("Not narcissistic numbers")
    def not_narcissistic_tests():
        dotest( 122, False)
        dotest(4887, False)
"""

"""
3. You are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
"""
def square_digits(num):
    # Your code here
    n = str(num)
    s = ""
    for i in range(len(n)):
        x = n[i]
        y = int(x) ** 2
        z = str(y)
        s += z
    return int(s)

#print(square_digits(9119))
# expect: 811181
"""#Alternative solution:
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)"""
"""
#Tests
import codewars_test as test
from solution import square_digits

@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
        test.assert_equals(square_digits(0), 0)
"""

"""
4. Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""
def disemvowel(string_):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for vowel in vowels:
        string_ = string_.replace(vowel, "")
    return string_


# print(disemvowel("This website is for losers LOL!"))
# expect: Ths wbst s fr lsrs LL!

"""
5. In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""
def high_and_low(numbers):
    numbers = numbers.split()
    list_num = []
    for number in numbers:
        list_num.append(int(number))
    largest = list_num[0]
    smallest = list_num[0]
    for i in range(1, len(list_num)):
        if list_num[i] > largest:
            largest = list_num[i]
    for i in range(1, len(list_num)):
        if list_num[i] < smallest:
            smallest = list_num[i]
    return f"{largest} {smallest}"


# print(high_and_low("1 2 3 4 5"))
# expect: 5 1
"""
Alternative solution:
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))
"""

"""
6. Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists,
such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

def dig_pow(n, p):
    string = str(n)
    sum_of_powers = 0
    i = 0
    for character in range(len(string)):
        power = int(string[character]) ** (p + i)
        sum_of_powers += power
        i += 1
    if sum_of_powers % n == 0:
        return int(sum_of_powers / n)
    else:
        return -1


# print(dig_pow(92, 1))
# expect: -1

"""
7. There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs.
Elements of each pair represent the number of people that get on the bus (the first item) and
the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array).
Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus,
they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0.
So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.
"""

def number(bus_stops):
    people_on_bus = 0
    people_off_bus = 0
    for index in range(len(bus_stops)):
        people_on_bus += bus_stops[index][0]
        people_off_bus += bus_stops[index][1]
    return people_on_bus - people_off_bus


# print(number([[10,0],[3,5],[5,8]]))  # [no._people_on, no._people_off]
# expect: 5

"""Alternative solution:
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])"""

"""
8. Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""
def is_triangle(a, b, c):
    # Triangle inequality theorem
    # Check if the sum of any two sides is greater than the third side
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


# print(is_triangle(2, 3, 4))
# expect: True
"""
9. Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        pairs.append(s[i:i + 2])
    if len(s) % 2 == 0:
        return pairs
    else:
        pairs[-1] += '_'
        return pairs


# print(solution("asdfads"))
# expect: ['as', 'df', 'ad', 's_']

"""
10. Bit Counting
Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case (there are 5 1s)
"""
def count_bits(n):
    return bin(n).count('1')  # bin returns binary representation of numbers;.count = # occurrences of whatever is in ()


# print(count_bits(1234))
# expect: 5
"""
11. You are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""
def alphabet_position(text):
    # ord() function returns the number representing the unicode code of a specified character
    # chr() function returns the character that represents the specified unicode
    result = ""
    for character in text:
        # checks if alphabet character
        if character.isalpha():
            position = ord(character.lower()) - ord('a') + 1
            result += str(position) + " "
    return result.strip()


# print(alphabet_position("The sunset sets at twelve o' clock."))
# expect: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

"""
MORSE CODE
12. Part 1
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and
digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−,
letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive,
traditionally capital letters are used.
When the message is written in Morse code, a single space is used to separate the character codes and
3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic),
that is coded as ···−−−···. These special codes are treated as single special characters,
and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Python: MORSE_CODE['.--']
"""
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
    '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}
# from preloaded import MORSE_CODE
def decode_morse(morse_code):
    morse = morse_code.strip().split(' ')
    message = ""
    for i, item in enumerate(morse):
        if item in MORSE_CODE:
            message += MORSE_CODE[item]
            # checks for 3 spaces between symbols to place a space in the message
            if i < len(morse) - 1 and morse[i + 1] == '':
                message += " "
    return message


# print(decode_morse('.... . -.--   .--- ..- -.. .'))
# expect: "HEY JUDE"

"""
MORSE CODE
12. Part 2
In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together,
which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of
"dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in fact different operators would
transmit at different speed.
An amateur person may need a few seconds to transmit a single character,
a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line
periodically, and if the line is connected (the key at the remote station is down), 1 is recorded,
and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received,
it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

110011001100110000001100000011111100110011111100111111000000000000001100111111001111110011111100000011001100111111000000
1111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line
exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message,
correctly decode the message to dots ., dashes - and spaces (one between characters, three between words)
and return those as a string.
Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them.
Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable
string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).

Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip
checking for errors and exceptions, just do your best in figuring out what the message is!
"""
def decode_bits(bits):
    bits = bits.strip("0")
    u = 0
    morse_code = ""
    count = 1
    for bit in bits:
        if bit != "0":
            u += 1
        else:
            break
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            count += 1
        else:
            if count < u:
                u = count
                count = 1
            else:
                count = 1
    words = bits.split("0"*7*u)
    for word in words:
        characters = word.split("0"*3*u)
        for character in characters:
            signs = character.split("0"*u)
            for sign in signs:
                if sign == "1"*3*u:
                    morse_code += "-"
                else:
                    morse_code += "."
            morse_code += " "
        morse_code += "   "
    return morse_code

def decode_morse(morseCode):
    morseCode.strip()
    result = ""
    characters = morseCode.split(" ")
    for character in characters:
        if character != "":
            result += MORSE_CODE[character]
        else:
            result += " "
    return " ".join(result.split())

bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
# morse_code = decode_bits(bits)
# print(morse_code)
# decoded_message = decode_morse(morse_code)
# print(decoded_message)  # Output: 'HEY JUDE'
# expect: ···· · −·−−   ·−−− ··− −·· · >> HEY JUDE

"""Alternative:
def decodeBits(bits):
    import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))
"""

"""
13. Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
Example:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    text = text.split()
    new_words = ""
    for i in range(len(text)):
        if text[i].isalpha():
            new_words += (text[i][1:] + text[i][0] + "ay" + " ")
        else:
            new_words += text[i] + " "
    return new_words.strip()


# print(pig_it("Pig latin is cool !"))

"""
# Alternative:
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""

"""
14. In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima)
of a numeric array.
For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays.
If there is no peak in the given array, then the output should be {pos: [], peaks: []}.
Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in
other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate
the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function,
we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not.
In case of a plateau-peak, please only return the position and value of the beginning of the plateau.
For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)
"""
def pick_peaks(arr):
    pos = []  # List to store the positions of peaks
    peaks = []  # List to store the values of peaks

    # Flag to keep track of potential plateau
    in_plateau = False
    # Variables to store plateau position and value
    plateau_pos = None
    plateau_val = None

    # Iterate through the array from the second element to the second-to-last element
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  # Potential peak found
            plateau_pos = i
            plateau_val = arr[i]
            in_plateau = True
        elif arr[i] < arr[i - 1] and in_plateau:  # Potential peak finalized
            pos.append(plateau_pos)
            peaks.append(plateau_val)
            in_plateau = False
            plateau_val = None  # Reset plateau value after each peak

    return {"pos": pos, "peaks": peaks}


print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
# Output: {"pos": [3, 7], "peaks": [6, 3]}

"""
# Alternative:
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
"""