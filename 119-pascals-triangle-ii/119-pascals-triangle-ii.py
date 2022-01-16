class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []        
        triangle.append([1])
        if rowIndex == 0: return triangle[0]
        for i in range(1,rowIndex+1):
            prevRow = triangle[i-1]
            currentrow = []
            currentrow.append(1)
            for j in range (1,len(prevRow)):
                currentrow.append(prevRow[j-1]+prevRow[j])
            currentrow.append(1)
            triangle.append(currentrow)
        return triangle[rowIndex]
        
        