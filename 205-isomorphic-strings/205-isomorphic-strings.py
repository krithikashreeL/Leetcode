class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        
        for i in range(len(s)):
            
            if (s[i] not in t_set) and (t[i] not in s_set) :
                t_set[s[i]] = t[i]
                s_set[t[i]] = s[i]
            elif t_set.get(s[i]) != t[i] or s_set.get(t[i]) != s[i]:
                    # print (s[i],t[i])
                    return False
        
        # print(s_set,t_set)
        return True