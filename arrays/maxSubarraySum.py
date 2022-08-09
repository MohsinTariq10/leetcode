from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    cum_sum = 0
    global_sum = 0
    
    for i in arr:
        cum_sum +=i
        if cum_sum < 0:
            cum_sum = 0
        global_sum = max(global_sum, cum_sum)
    return global_sum
