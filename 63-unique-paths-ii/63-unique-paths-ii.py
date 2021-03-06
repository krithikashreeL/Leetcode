class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        #dp = [[0]*n]*m
        
        dp=[[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
		
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
			
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    
                    
                    
        
        return dp[-1][-1]