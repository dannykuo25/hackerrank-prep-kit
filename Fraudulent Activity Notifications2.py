#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.

def getTwiceMid(d, count, medianPos):
    # create acc
    acc = [0] * 201
    for i in range(1, len(acc)):
        acc[i] = acc[i-1] + count[i]
    # print(acc)
    # odd
    if d % 2 == 1:
        for i in range(len(acc)):
            if acc[i] >= medianPos:
                return 2 * i
    # even
    else:
        a, b = None, None
        for i in range(len(acc)):
            if acc[i] >= medianPos and a is None:
                a = i
            if acc[i] >= medianPos + 1:
                b = i
                break
        return a + b
# 12 5
# 0 1 2 3 4 5 6 7 8  9 10 11 index
# -----------------------------------
# 6 4 9 2 1 2 4 6 7 15  4  6 expenditure

# 0 1 1 0 1 0 1 0 0  1  0  0 count

# 0 1 2 2 3 4 5 5 5  6  6  6 acc
# 
# mid

def activityNotifications(expenditure, d):
    alert = 0
    n = len(expenditure)
    count = [0] * 201
    # create count array
    for i in range(d):
        count[expenditure[i]] += 1
    # determine odd or even median position
    if d % 2 == 0:
        medianPos = int(d/2)
    else:
        medianPos = int(d/2) + 1

    for i in range(d, n):
        median = getTwiceMid(d, count, medianPos)
        # print(mid)
        if expenditure[i] >= median: 
            alert += 1
        # update count array
        count[expenditure[i]] += 1
        count[expenditure[i-d]] -= 1
    return alert
# 12 6
# 0 1 2 3 4 5 6 7 8  9 10 11 index
# -----------------------------------
# 6 4 9 2 1 2 4 6 7 11  4  6 expenditure
# 0 0 1 0 2 0 1 1 0  0  0  1 count
# 0 0 1 1 3 3 4 5 5  5  5  6 acc
# i == 11
# mid == 10
# alert == 3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
