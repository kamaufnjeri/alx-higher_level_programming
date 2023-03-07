#!/usr/bin/python3
for num1 in range(0, 10):
    if num1 == 8:
        print(89)
    else:
        for num2 in range(num1 + 1, 10):
            print("{}{}".format(num1, num2), end=", ")

