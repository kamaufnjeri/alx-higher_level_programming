#!/usr/bin/python3

if __name__ == "__main__":
    """Print addition of all arguments"""
    import sys

    add = 0
    count = len(sys.argv) - 1
    if count == 0:
        print(0)
    else:
        for i in range(count):
            add += int(sys.argv[i + 1])
    print(add)
