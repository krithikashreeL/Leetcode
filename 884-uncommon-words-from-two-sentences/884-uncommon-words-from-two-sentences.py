class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}
        
        count = collections.Counter(s1.split())
        count += collections.Counter(s2.split())
        return [word for word in count if count[word] == 1]
        