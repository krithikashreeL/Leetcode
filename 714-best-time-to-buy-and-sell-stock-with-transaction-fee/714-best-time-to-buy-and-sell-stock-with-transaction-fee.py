class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <=1 : return 0
        nostock = 0
        onestock = -prices[0]
        for i in range(1,len(prices)):
            nostock = max(nostock,onestock+prices[i]-fee)
            onestock = max(onestock,nostock-prices[i])
        return nostock