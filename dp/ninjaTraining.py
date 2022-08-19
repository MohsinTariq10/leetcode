from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1]*4 for i in range(n)]
    return recur(points, n-1, 3, dp)

def recur(points, days, last, dp):
    maxi = 0
    if days == 0:
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[days][i])
        return maxi
    if dp[days][last] == -1:
        for i in range(3):
            if i != last:
                maxi = max(points[days][i] + recur(points, days-1, i, dp), maxi)
        dp[days][last] = maxi
    return dp[days][last]

from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[-1]*4 for x in range(n)]
    dp[0][0] = max(points[0][1:])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][:2])
    dp[0][3] = max(points[0])
    
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if last != task:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], point)
    return dp[n-1][-1]
                    
                    
                    