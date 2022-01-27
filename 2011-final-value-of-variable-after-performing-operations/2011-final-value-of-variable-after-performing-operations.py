class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in range(0,len(operations)):
            
            if "--" in str(operations[i]):
                value -= 1
            else:
                value += 1
        return value
        