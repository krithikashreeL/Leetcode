class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is "": return 1
        palindrome_check = ""
        for letter in s:
            if letter.isalnum():
                palindrome_check += letter
       
        return (palindrome_check.lower() == palindrome_check[::-1].lower())
                
        