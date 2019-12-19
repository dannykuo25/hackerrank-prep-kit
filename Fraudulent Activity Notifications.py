#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
# brute force
# def mid(arr):
#     arr.sort()
#     if len(arr) % 2 == 1:
#         return arr[len(arr) // 2]
#     return (arr[(len(arr)//2)-1] + arr[len(arr)//2])/2

# def activityNotifications(expenditure, d):
#     result = 0
#     for i in range(d, len(expenditure)):
#         if expenditure[i] >= mid(expenditure[i-d: i]) * 2:
#             result += 1
#     return result

# count sort method
def activityNotifications(expenditure, d):
    

# 9 5
# 2 3 4 2 3 6 8 4 5

# calculate mid
# 2 2 3 3 4 = 3, 3*2 == 6, result == 1
# 3 4 2 3 6 ->sorted -> 2 3 3 4 6, mid = 3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
