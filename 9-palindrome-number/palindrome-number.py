from math import log10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0: 
            return False
        
        original = x
        result = 0

        while original>0:
            current_value = original % 10
            result = result * 10 + current_value
            original = original // 10

        return x == result