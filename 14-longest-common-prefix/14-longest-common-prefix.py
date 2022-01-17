class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key= len)
        if len(strs) == 0 or len(shortest_str) == 0:
            return ""
        
        prefix = ""
        for i in range(len(shortest_str)):
            for s in strs:
                if shortest_str[i] != s[i]:
                    return prefix
            prefix += shortest_str[i]
            #print(shortest_str[:i+1])
        
        return prefix