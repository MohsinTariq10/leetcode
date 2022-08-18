def func(ind, arr, buff, res, n):
    if ind >= n:
        return res.append(buff[:])
        
    buff.append(arr[ind])
    func(ind+1, arr, buff,res, n)
    buff.pop()
    func(ind+1, arr, buff,res, n)
    return res

print(func(0, [3,1,2], [], [], 3))