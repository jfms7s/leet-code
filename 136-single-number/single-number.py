from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mask = 0

        for i in nums:
            mask = mask ^ i

        return mask
        