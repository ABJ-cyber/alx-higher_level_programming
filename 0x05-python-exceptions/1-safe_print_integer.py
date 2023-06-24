#!/usr/bin/python3


def safe_print_integer(value):
    """ Print an integer
        Args:
            value (int): integer to print
        Returns:
            True if integer, else false
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
