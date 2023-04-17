#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 3)
    r1.display()

    print("---")

    r1 = Rectangle(5, 2)
    r1.display()
