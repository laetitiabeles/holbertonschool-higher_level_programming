#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(1, 101):
        if abs(numbers) % 15 == 0:
            print("FizzBuzz", end=" ")
        elif abs(numbers) % 3 == 0:
            print("Fizz", end=" ")
        elif abs(numbers) % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(numbers, end=" ")
