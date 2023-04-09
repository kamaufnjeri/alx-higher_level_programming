 #!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print(value)
            return True
    except TypeError:
        return False
