class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num != 0:
            i = i + 1 
            
            if (num % 2) == 0:
                num = num / 2
            else:
                num = num - 1
        
        return i

        