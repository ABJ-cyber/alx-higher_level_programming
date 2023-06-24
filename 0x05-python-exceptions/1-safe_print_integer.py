#!/usr/bin/python3
""" prints an integer """

def safe_print_integer(value):
	try:
		print("{:d}".format(value))
	except ValueError:
		return False

	return True


