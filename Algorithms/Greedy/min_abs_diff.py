#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    if len(arr) > 1:
        arr.sort()
        minDist = abs(arr[1] - arr[0])
        for i in range(1, len(arr) - 1):
            curDist = abs(arr[i] - arr[i+1])
            if curDist < minDist:
                minDist = curDist
    return minDist

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
