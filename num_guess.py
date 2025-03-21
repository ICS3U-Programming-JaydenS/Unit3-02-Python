#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This programs makes the user see if they can get the same number with the random number constants
import constants


def main():
    # Get the users guess
    user_guess = int(input("Pick a number from 1-9:"))
    # Checks if the user got it right
    if user_guess == constants.RANDOM_NUMBER:
        print("You got it right!")
    # if not then this displays
    if user_guess != constants.RANDOM_NUMBER:
        print("Wrong try again!")


if __name__ == "__main__":
    main()
