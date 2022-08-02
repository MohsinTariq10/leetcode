def nextSmallerElement(arr,n):
    # Write your code here.
    stack = [arr[-1]]
    res= [-1 for x in range(n)]
    i = n-2
    while(i>-1):
#         print(stack)
        if stack and stack[-1] < arr[i]:
            res[i] = stack[-1]
            stack.append(arr[i])
        else:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])
        i-=1
    return res    
    