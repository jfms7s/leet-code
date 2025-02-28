class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        i = 0
        while target != 1 and  maxDoubles > 0:
            i = i + 1 
            
            if (target % 2) == 0:
                maxDoubles = maxDoubles - 1
                target = target // 2
            else:
                target = target - 1
        
        return i + target - 1

        