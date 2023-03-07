#!/usr/bin/python3
for num in range(1, 101):
    elif (num % 5 == 0) and (num % 3 == 0):
        print("FizzBuzz", end=" ")
    elif (num % 5 == 0):
        print("Buzz", end=" ")
    elif (num % 3 == 0):
        print("Fizz", end=" ")
    else:
        print(f"{num}", end=" ")
