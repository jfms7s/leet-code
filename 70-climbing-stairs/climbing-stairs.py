class Solution:
    caching = {
        0:0,
        1:1,
        2:2,
    }
    def climbStairs(self, n: int) -> int:
        
        if n in Solution.caching:
            return Solution.caching[n]
        
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        Solution.caching[n] = result
        return result