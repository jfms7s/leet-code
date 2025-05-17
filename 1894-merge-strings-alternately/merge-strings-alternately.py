class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        size1 = len(word1)
        size2 = len(word2)

        min_size = min(size1, size2)
        result = ""

        for i in range(min_size):

            result += word1[i] + word2[i]

        result += word1[min_size:size1] + word2[min_size:size2]

        return result