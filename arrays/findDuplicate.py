def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    t = arr[arr[0]]
    h = arr[arr[arr[0]]]
    
    while h!=t:
        t = arr[t]
        h = arr[arr[h]]
        
    t = arr[0]
    while h!=t:
        t = arr[t]
        h = arr[h]
    return h