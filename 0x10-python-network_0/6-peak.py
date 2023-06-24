#!/usr/bin/python3
"""finds peak in a list"""

def find_peak(list_of_integers):
    "finds and returns peak"
    arr = list_of_integers
    n = len(list_of_integers)
    start = 0
    end = n - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    if start >= n:
        return None
    return arr[start]
