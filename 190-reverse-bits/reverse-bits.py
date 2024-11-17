class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        mask = 1
        for i in range(32):
            current = n & mask
            n = n >> 1  
            result = result << 1
            result |= current

        return result


