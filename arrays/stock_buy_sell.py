class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        profit = 0
        buy = prices[0]
        n = len(prices)
        for i in range(1,n):
            if profit < prices[i] - buy:
                profit = prices[i] -  buy
            if buy > prices[i]:
                buy = prices[i]
        return profit