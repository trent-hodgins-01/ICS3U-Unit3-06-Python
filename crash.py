# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/23/2021
# This is the Crash program
# The user enters in the number of a month and the program tells them the month


import random


def main():
    # this function checks to see if the user guessed the correct number
    random_number = random.randint(1, 100)
    # a number between 1 and 100

    # input
    guessed_number = input("Guess a number between 0 and 100 (integer): ")
    print("")

    # process and output
    try:
        integer_as_number = int(guessed_number)
        if random_number == integer_as_number:
            print("You Guessed Correctly")
        else:
            print("You Guessed Wrong! Correct answer was {0}".format(random_number))

    except Exception:
        print("You didn’t enter in an integer.")
    finally:
        print("\nThanks for playing!")

    print("\nDone")


if __name__ == "__main__":
    main()
