from os import *
from sys import *
from collections import *
from math import *

# [2, 1 3 4] 2
# [4, 3, 2, 1] 0

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    i = n-1
    while(i > 0):
        if permutation[i-1] < permutation[i]:
            break
        i -= 1
    
    pivot = i - 1
    p_elem = permutation[pivot]
    j = i
    n_g = i
    while(j < n):
        if permutation[j] > p_elem:
            if permutation[n_g] > permutation[j]:
                n_g  = j
        j+=1
    permutation[n_g], permutation[pivot] = permutation[pivot],  permutation[n_g]
    permutation[i:] = sorted(permutation[i:])
    
    return permutation