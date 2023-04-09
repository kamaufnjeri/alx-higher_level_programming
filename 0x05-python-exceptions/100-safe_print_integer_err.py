#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as msg:
        sys.stderr.write("{}".format(msg))
        return False
