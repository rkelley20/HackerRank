#!/bin/python3

import sys

def camelcase(s):
    if len(s) == 0: return 0
    return len([x for x in s if x.isupper()]) + 1
                

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
