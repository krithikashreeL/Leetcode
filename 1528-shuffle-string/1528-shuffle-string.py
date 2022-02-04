class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = ''
        for i in range(0,len(indices)):
            new_s +=   s[indices.index(i)]
        
            
           
        
        return new_s