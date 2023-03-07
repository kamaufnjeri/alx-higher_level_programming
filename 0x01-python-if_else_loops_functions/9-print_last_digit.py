#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
    else:
        number *= -1
        last = number % 10
    print(last, end="")
    return(last)
