#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the average of 10 random numbers


import random


def main():

    ten_numbers = []
    print("Here are 10 numbers:")

    for loop_counter in range(1, 10):
        random_numbers = random.randint(1, 100)
        ten_numbers.append(random_numbers)
        print(random_numbers)

    average_value = (sum(ten_numbers)) / 10

    print("The average is {0}".format(average_value))


if __name__ == "__main__":
    main()
