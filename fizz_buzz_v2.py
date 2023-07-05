# FizzBuzz Program

# returns main fizzbuzz program
def fizzbuzz(number):
    # prints 'fizzbuzz' for no.s divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        return print('FizzBuzz')

    # prints 'buzz' for no.s divisible by 5
    elif number % 5 == 0:
        return print('Buzz')

    # prints 'fizz' for no.s divisible by 3
    elif number % 3 == 0:
        return print('Fizz')

    # print no.s that are not divisible by 3 or 5
    else:
        return print(number)


# selects range from 1 to 100 to iterate through
for number in range(1, 101):
    fizzbuzz(number)
