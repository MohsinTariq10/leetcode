import heapq
def slidingWindowMaximum(nums:list, k:int):
# Write your code here
# Return a list
    n = len(nums)
    if k == n: return [max(nums)]
    if k == 1: return nums
    res = []
    q = []
    start, end = 0, 0

    while(end < n):
        elem = nums[end]
        
        if not q or q[0] < elem:
            while q and q[0] < elem:
                q.pop(0)    
            q.insert(0, elem)
        else:
            while q and q[-1] < elem:
                q.pop()
            q.append(elem)
        
        if end+1-start == k:
            res.append(q[0])
            if q[0] == nums[start]:
                q.pop(0)
            start+=1
            end+=1
        else:
            end+=1
    return res