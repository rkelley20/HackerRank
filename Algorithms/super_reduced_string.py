#!/bin/python3

import sys

def super_reduced_string(s):
    if len(s) == 0: return "Empty String"
    stack = ""
    for i in range(0, len(s) - 1):
        if s[i] == s[i+1]: 
            stack += s[i+2:len(s)]
            return super_reduced_string(stack)
        else:   stack += s[i]
    return s

s = input().strip()
result = super_reduced_string(s)
print(result)
