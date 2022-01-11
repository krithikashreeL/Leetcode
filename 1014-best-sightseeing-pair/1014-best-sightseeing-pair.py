class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        currentmaxscore = values[0]+0
        maxscore = 0
        n = len(values)
        for i in range(1,n):
            maxscore = max(maxscore,currentmaxscore+values[i]-i)
            print(max(currentmaxscore, currentmaxscore+values[i]-i))
            currentmaxscore = max(currentmaxscore,values[i]+i)
        return maxscore

        
        