class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count_word1 = {}
        count_word2 = {}
        
        for word in words1:
            count_word1[word] = count_word1.get(word,0)+1
            
        for word in words2:
            count_word2[word] = count_word2.get(word,0)+1
        count = 0
        for word in count_word1:
            if word in count_word2 and count_word1[word] == count_word2[word]== 1:
                count+=1
        return count
        