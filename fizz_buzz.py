"""
Activy as shown in README.md
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:   # Looks for multiples of 3 and 5 by dividing and checking for a remainder of 0
        print("FizzBuzz")
    elif number % 5 == 0:  # Looks for multiples of 5 by dividing and checking for a remainder of 0
        print("Buzz")
    elif number % 3 == 0:  # Looks for multiples of 3 by dividing and checking for a remainder of 0
        print("Fizz")
    else:
        print(number)  # Prints the numbers that are exceptions of the above conditions