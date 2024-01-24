#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10

if last_d < 0:
    last_d = -last_d

if last_d > 5:
    end_string = "is greater than 5"
elif last_d == 0:
    end_string = "is 0"
elif last_d < 6 and last_d != 0:
    end_string = "is less than 6 and not 0"

print(f"Last digit of {number} is {last_d} and {end_string}")
