class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n < 0 : 
            neg = True
            n = -1 * n
        res = 1
        
        while (n>0):
            if n%2 == 1:
                res *= x
            x*=x
            n = int(n/2)
        
        if neg: res = 1/res
        return res