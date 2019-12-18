#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    result = []
    dic = {}
    freqDic = {}
    for query in queries:
        print('query=', query)
        # insert
        if query[0] == 1:
            if query[1] not in dic:
                dic[query[1]] = 1
                if 1 in freqDic:
                    freqDic[1] += 1
                else:
                    freqDic[1] = 1
            else:
                freqDic[dic[query[1]]] -= 1
                if dic[query[1]] + 1 in freqDic:
                    freqDic[dic[query[1]] + 1] += 1
                else:
                    freqDic[dic[query[1]] + 1] = 1
                dic[query[1]] += 1

        # delete
        elif query[0] == 2:
            if query[1] in dic:
                if dic[query[1]] >= 1:
                    freqDic[dic[query[1]]] -= 1
                    dic[query[1]] -= 1
        # check freq
        else:
            if query[1] not in freqDic:
                result.append(0)
            else:
                if freqDic[query[1]] > 0:
                    result.append(1)
                else:
                    result.append(0)
    return result


if __name__ == '__main__':

    OUTPUT_PATH = "input5"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
