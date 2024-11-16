from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counter = Counter(nums)
        for value,count in counter.items():
            if count == 1:
                return value
        