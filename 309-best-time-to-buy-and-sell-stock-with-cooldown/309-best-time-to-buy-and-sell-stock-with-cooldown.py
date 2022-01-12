class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -math.inf
        sold = rest = 0
        for i in prices:
            temphold = max(hold,rest-i)
            tempsold = hold+i
            temprest = max(rest,sold)
            hold = temphold
            sold = tempsold
            rest = temprest
        return max(rest,sold)
        
        
        