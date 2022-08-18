def countDistinctWays(n: int) -> int:
    a, b = 1, 2
    if n == 0 or n == 1: return 1
    if n == 2: return 2
    for i in range(2,n):
        t = a + b
        a, b = b, t
    return t