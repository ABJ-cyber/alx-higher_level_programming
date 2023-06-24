#!/usr/bin/python3


def find_peak(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start
