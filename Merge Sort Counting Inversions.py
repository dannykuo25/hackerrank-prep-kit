#!/bin/python3

import math
import os
import random
import re
import sys


def mergesort(arr, swapCount):
    if len(arr) > 1:
        mid = len(arr) // 2 # 3
        L = arr[:mid] # 38 27 43 
        # print(L)
        R = arr[mid:] # 3 9 82 10
        # print(R)
        mergesort(L, swapCount)
        mergesort(R, swapCount)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                originalPos = len(L) + j
                swapCount[0] += originalPos - k
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Complete the countInversions function below.
def countInversions(arr): # 38 27 43 3 9 82 10
    swapCount = [0]
    mergesort(arr, swapCount)
    return swapCount[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
