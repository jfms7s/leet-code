class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        sign = 1
        index = len(digits) - 1
        while(index > -1):

            result = digits[index] + sign
            sign = result//10
            digits[index] = result % 10
            index -= 1
        if sign:
            digits.insert(0,1)
        return digits