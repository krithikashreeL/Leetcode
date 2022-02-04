class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for sentence in sentences:
            sentence = sentence.split(" ")
            if len(sentence) > max_len:
                max_len = len(sentence)
        return max_len
        