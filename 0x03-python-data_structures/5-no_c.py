#!/usr/bin/python3

def no_c(my_string):
    new = ""
    for letter in my_string:
        if letter != "C" or letter != 'c':
            new += letter
    return new
