#!/bin/python3

import sys

def marsExploration(s):
    sos = "SOS"
    ptr = 0
    total = 0
    for c in s:
        if c != sos[ptr]:
            total += 1
        ptr += 1
        if ptr > len(sos) - 1:
            ptr = 0
    return total
            

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
