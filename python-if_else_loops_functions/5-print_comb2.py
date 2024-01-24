#!/usr/bin/python3
for numbers in range(100):
    if numbers < 10:
        print(f"0{numbers}, ", end="")
    elif numbers == 99:
        print(numbers)
    else:
        print(f"{numbers}, ", end="")
