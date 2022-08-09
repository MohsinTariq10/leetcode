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

def maximumProfit(prices):
    # Write your code here.
    buy = 0
    sell = 1
    max_profit = 0
    while(buy < len(prices) and sell < len(prices)):
        profit = prices[sell] - prices[buy]
        max_profit = max(profit, max_profit)
        if profit < 0:
            buy = sell

        sell +=1
    return max_profit