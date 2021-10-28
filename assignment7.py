#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program checks whether an element occurs in a list

import random


def check(integer_from_user, random_list):
    # This function checks if a number is in the list

    if integer_from_user in random_list:
        is_it_there = 0
    else:
        is_it_there = 1

    return is_it_there


def main():

    generated_random_list = []

    for counter in range(0, 10):
        random_number = random.randint(1, 25)
        generated_random_list.append(random_number)

    user_input = input("What integer are you searching for? (0-25): ")

    try:
        user_integer = int(user_input)
        is_the_number_in_list = check(user_integer, generated_random_list)
        if is_the_number_in_list == 0:
            print("\nThe number {0} is in the list.".format(user_integer))
        else:
            print("\nThe number {0} is not in the list.".format(user_integer))
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
