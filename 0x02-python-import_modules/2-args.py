#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if (len(sys.argv) - 1) == 0:
        print("0 arguments.")
    elif (len(sys.argv) - 1) == 1:
        print("1 argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for i in range(len(sys.argv) - 1):
        print(f"{i + 1}: {sys.argv[i + 1]}")
