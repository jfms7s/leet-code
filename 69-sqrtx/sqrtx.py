class Solution:
    def mySqrt(self, x: int) -> int:

        high = x
        low = 1
        while high>=low:
            mid = (high+low)//2
            result = mid*mid
            if result == x:
                return mid
                
            if x > result:
                low = mid + 1
            else:
                high = mid -1

        return high