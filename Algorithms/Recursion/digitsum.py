#!/bin/python3

import sys       

def digitSum(n, k):
    # Complete this function
    if len(n) == 1: return n
    else:
        total = sum([int(x) for x in n]) * k
        return digitSum(str(total), 1)


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)
