#!/usr/bin/python3
"""
write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    
    x = 0
    y = 2
    while n > 1:
        while not n % y:
            x += y
            n /= y
        y += 1
    return x
