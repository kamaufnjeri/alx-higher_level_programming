#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0

    for i in my_list:
        y += 1

    class larger(Exception):
        def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)
    try:
        if x < y:
            for n in my_list[:x]:
                print(n, end="")
            print()
            return x
        else:
            raise larger
    except larger:
        for n in my_list[:x]:
            print(n, end="")
        print()
        return y
