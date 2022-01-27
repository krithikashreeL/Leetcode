class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        output =''
        for i in range(0,len(str_list)-1):
            temp = str_list[i]
            output+= temp[::-1] + " "
        temp = str_list[len(str_list)-1]
        output += temp[::-1]
        return output