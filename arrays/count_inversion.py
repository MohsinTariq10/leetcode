from os import *
from sys import *
from collections import *
from math import *

def merge_sorted_arrays(a1, a2, inv):
    count = 0
    lena1 = len(a1)
    a1_guzra = 0
    total = 0
    a1 = a1 + [0] * len(a2)
    insertions = 0
    for elem in a2:
        while(count < len(a1)+len(a2)):
            if a1[count] == 0 and count < (insertions + len(a1)):
                a1[count] = elem
                count += 1
                break
            elif elem > a1[count]:
                count+=1
                a1_guzra +=1
            elif elem == a1[count]:
                a1.pop(-1)
                a1.insert(count, elem)
                count+=1
                total += lena1 - a1_guzra-1
                insertions +=1
                break
            else:
                a1.pop(-1)
                a1.insert(count, elem)
                count+=1
                insertions +=1
                total += lena1 - a1_guzra
                break
    return a1, total + inv
                
def merge_sort(arr, inv):
    length = len(arr)
    
    if length > 1:
        l = int(length/2)
        a1, inv = merge_sort(arr[:l], inv)
        a2, inv = merge_sort(arr[l:], inv)
        return merge_sorted_arrays(a1, a2, inv)
    else:
        return arr, inv
        
    
def getInversions(arr, n) :
#     print(merge_sorted_arrays([1,2], [3,4]))
	# Write your code here.
    inv = 0
    arr, inv = merge_sort(arr, inv)
    return inv
# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))