# Refactored Movie Rating Program

# verifies age input
def verify_age():
    while True:
        age = input("Please enter your age: ")
        # check if the input is a digit
        if not age.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        # convert the age to an integer
        customer_age = int(age)
        # check if the age is within the limits
        if customer_age < 0 or customer_age > 117:
            print("Invalid age. Please enter your actual age.")
        else:
            break
    return customer_age


# returns which movie ratings the user is allowed to watch
def get_movie_ratings_user_can_watch(customer_age):
    if customer_age < 12:
        return 'U and PG movies are available.'
    elif customer_age <= 12:
        return 'U, PG, 12 movies are available.'
    elif customer_age <= 15:
        return 'U, PG, 12, 15 movies are available.'
    else:
        return 'All movies are available, including: U, PG, 12, 15, 18 rated movies.'


# calls verify_age function to get user age
customer_age = verify_age()

# calls get_movie_ratings_user_can_watch
movie_rating = get_movie_ratings_user_can_watch(customer_age)
print(movie_rating) # prints list of movie ratings available to watch
