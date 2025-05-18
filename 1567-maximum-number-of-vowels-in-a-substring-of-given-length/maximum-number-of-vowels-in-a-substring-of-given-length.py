class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left = 0
        right = k
        counter = 0
        size = len(s)
        
        for i in range(k):

            counter += int(s[i] in "aeiou")
        
        max_val = counter

        while right < size:

            counter += int(s[right] in "aeiou") - int(s[left] in "aeiou")

            max_val = max(max_val, counter)
            right += 1
            left += 1
        return max_val