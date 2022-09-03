class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = prices[0]
        
        for i in range (1,len(prices)):
            if min_profit > prices[i]:
                min_profit = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-min_profit)
        return max_profit
        