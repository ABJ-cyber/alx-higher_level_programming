#!/usr/bin/python3
""" prints an integer """

def safe_print_integer(value):
	try:
		print("{value:d}".format(value=value))
	Except valueError:
		return False

	return True


