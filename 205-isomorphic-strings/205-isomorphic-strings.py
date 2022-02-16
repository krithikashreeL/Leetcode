class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s ={}
        map_t = {}
        n = len(s)
        m = len(t)
        if m != n : return False
        for i in range(0,n):
            if((s[i] not in map_s) and (t[i] not in map_t)):
                map_s[s[i]] = t[i]
                map_t[t[i]] = s[i]
            elif map_s.get(s[i]) != t[i] or map_t.get(t[i])!= s[i]:
                return False
        return True
        
        
        