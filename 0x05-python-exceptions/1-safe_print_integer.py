#!/usr/bin/python3
""" prints an integer """

def safe_print_integer(value):
	try:
		print("{value:d}".format(value=value))
	except ValueError:
		return False

	return True


