#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    res = [0 ,0]
    # Comparing the triplets using if - else condition, is there a better way
    if a0 > b0:
        res[0] += 1
    elif a0 < b0:
        res[1] += 1
    if a1 > b1:
        res[0] += 1
    elif a1 < b1:
        res[1] += 1
    if a2 > b2:
        res[0] += 1
    elif a2 < b2:
        res[1] += 1
    return res

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))