class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current = 0
        max_alt = 0 
        
        for i in gain:
            current += i
            max_alt = max(max_alt, current)

        return max_alt
