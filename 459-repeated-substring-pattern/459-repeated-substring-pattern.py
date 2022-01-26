class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1,n):
            if n%i == 0:
                sub_string = s[0:i]
                repeats = n//i
                if sub_string*repeats == s:
                    return True
        return False
            
        