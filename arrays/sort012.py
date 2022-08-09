from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    pz = 0
    p2 = n-1
    pc = 0
    
    while(pc < n):
        if arr[pc] == 0 and pc > pz:
            arr[pc], arr[pz] = arr[pz], arr[pc]
            pz+=1
        elif arr[pc] == 2 and pc < p2:
            arr[pc], arr[p2] = arr[p2], arr[pc]
            p2-=1
        else:
            pc+=1
    return arr
