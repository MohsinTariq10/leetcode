#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMaximumSustainableClusterSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processingPower
#  2. INTEGER_ARRAY bootingPower
#  3. LONG_INTEGER powerMax
#

def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    # Write your code here
    n = len(processingPower)
    i = 0
    j = 0
    sum_ = 0
    q = []
    res = 0
    while(j < n):
        sum_ += processingPower[j]
        print(q)
        while(q and q[-1][0] <= bootingPower[j]):
            q.pop()
        q.append((bootingPower[j], j))
        while(i <= j and (q[0][0] + sum_*(j-i+1)) > powerMax ):
            if(q[0][1] == i):
                q.pop(0)
            sum_ -= processingPower[i]
            i+=1
        res = max(res, j-i+1)
        j+=1
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    processingPower_count = int(input().strip())

    processingPower = []

    for _ in range(processingPower_count):
        processingPower_item = int(input().strip())
        processingPower.append(processingPower_item)

    bootingPower_count = int(input().strip())

    bootingPower = []

    for _ in range(bootingPower_count):
        bootingPower_item = int(input().strip())
        bootingPower.append(bootingPower_item)

    powerMax = int(input().strip())

    result = findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax)

    fptr.write(str(result) + '\n')

    fptr.close()
