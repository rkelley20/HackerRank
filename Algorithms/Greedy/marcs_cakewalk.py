#!/bin/python3

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for i in range(len(calorie)):
        miles += calorie[i] * 2**i
    return miles
        

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)
