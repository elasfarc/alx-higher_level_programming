#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
isNegative = number < 0
last_digit = (number % 10) if not isNegative else ((number * -1) % 10) * -1


msg = F"Last digit of {number:d} is {last_digit:d} and is"

if last_digit > 5:
    print(msg, "greater than 5")
elif last_digit == 0:
    print(msg, "0")
else:
    print(msg, "less than 6 and not 0")
