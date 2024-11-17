class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0:
            bit = n & 1
            if bit:
                counter += bit
            n >>= 1

        return counter