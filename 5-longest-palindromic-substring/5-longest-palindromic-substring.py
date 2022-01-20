class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1 : return s
        
        def expand_from_mid(left_index,right_index):
            while (left_index >= 0 and right_index < n and s[left_index] == s[right_index]):
                left_index -=1
                right_index +=1
            return right_index-left_index-1
        
        start_position = end_position = 0
        
        for i in range (n):
            len1 = expand_from_mid(i,i)
            len2 = expand_from_mid(i,i+1)
            max_len = max(len1,len2)
            if max_len > end_position - start_position :
                end_position = i + max_len //2
                start_position = i -(max_len - 1) //2
        return s[start_position:end_position+1]
                
            
        
            
        