#!/bin/python3

import sys

def camelcase(s):
    if len(s) == 0: return 0
    total = 1
    for x in s:
        if x.isupper(): total += 1
    return total
                

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
