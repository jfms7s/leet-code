class Solution:
    def numSteps(self, s: str) -> int:
        overflow = 0
        count = 0
        i = len(s) -1
        while i > 0 :
            current_value = (ord(s[i])-ord("0")) + overflow
            overflow = current_value >> 1
            
            if current_value & 1 :
                overflow = 1
                count = count + 2
            else:
                count = count + 1
            i = i - 1

        return count + overflow