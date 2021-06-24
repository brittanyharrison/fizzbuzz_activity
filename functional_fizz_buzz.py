"""
Below you can find my answer to the activity as shown in the README.md.
"""


def multiple_of_three(
        three_sub=input("What word would you like to substitute for multiples of 3?"),  # User prompt for sub words
        five_sub=input("What word would you like to substitute for multiples of 5?"),
        three_five_sub=input("What word would you like to substitute for multiples of 3 and 5?")):
    for number in range(1, 101):  # Gives a range of numbers from 1-100
        if number % 3 == 0 and number % 5 == 0:  # Looks for multiples of 3 and 5 by dividing and checking for a remainder of 0
            print(three_five_sub)
        elif number % 5 == 0:  # Looks for multiples of 5 by dividing and checking for a remainder of 0
            print(five_sub)
        elif number % 3 == 0:  # Looks for multiples of 3 by dividing and checking for a remainder of 0
            print(three_sub)
        else:  # Prints the numbers that are exceptions of the above conditions
            print(number)


print(multiple_of_three())
