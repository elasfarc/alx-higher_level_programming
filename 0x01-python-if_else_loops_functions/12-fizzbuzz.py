#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 == 0 or num % 5 == 0):
            if num % 3 == 0:
                print("Fizz", end="")
            if num % 5 == 0:
                print("Buzz", end="")
        else:
            print("{}".format(num), end="")
        print(" ", end="")
