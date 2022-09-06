class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        
        for i in range(0,len(ops)):
            if ops[i] == 'D':
                result.append(result[-1] * 2)        
            elif ops[i] == 'C':
                result.pop()           
            elif ops[i] =='+':
                result.append(result[len(result) - 1]+ result[len(result) - 2])
            
            else:
                result.append(int(ops[i]))
                
        # print((result))
        
        return sum(result)
        
        