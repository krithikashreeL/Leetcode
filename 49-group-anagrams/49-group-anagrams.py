class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for string in strs:
            sorted_string = sorted(string)
            sorted_string = tuple(sorted_string)
            if sorted_string in dict:
                dict[sorted_string].append(string) 
            else:
                dict[sorted_string] = [string]
        return dict.values()
            
        