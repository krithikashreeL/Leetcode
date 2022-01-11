class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = prices[0]
        n = len(prices)
        for i in range(0,n):
            if prices[i] < min_profit:
                min_profit = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-min_profit)
        return max_profit
        