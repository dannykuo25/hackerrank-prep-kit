#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
# incomplete solution
def countTriplets(arr, r):
    result = 0
    dic = {}
    # create a dic
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    print(dic)
    for num in dic:
        print('num=', num)
        # corner case
        if r == 1:
            if dic[num] >= 3:
                result += (dic[num] * (dic[num] - 1) * (dic[num] - 2)) // 6
        else:
            if num * r in dic:
                if num * r * r in dic:
                    result += dic[num] * dic[num * r] * dic[num * r * r]
    return result

# time: O(n), space: O(n)
def countTriplets(arr, r):
    result = 0
    dic1 = {}
    dic2 = {}
    for num in arr:
        if num / r in dic2:
            result += dic2[num / r]

        if num / r in dic1:
            if num in dic2:
                dic2[num] += dic1[num / r]
            else:
                dic2[num] = dic1[num / r]
        
        if num in dic1:
            dic1[num] += 1
        else:
            dic1[num] = 1
            
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
