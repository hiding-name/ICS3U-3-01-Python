#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program adds numbers


def main():
    # funciton adds numbers

    # Welcome statement
    print("NUMBER CALCULATOR 3000")
    print("Welcome, this is the Number Calculator 3000!")
    input("Press Enter to continue.")

    # input
    number = float(input("\nWhat is the first number: "))
    number1 = float(input("What is the other number: "))

    # process
    answer = number + number1

    # output
    print("The answer is: " + str(round(answer, 2)))


if __name__ == "__main__":
    main()
