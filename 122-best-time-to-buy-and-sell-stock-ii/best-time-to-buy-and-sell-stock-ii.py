class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(1,len(prices)):
            potencial = prices[i] - prices[i-1]
            profit += potencial if potencial > 0 else 0

        return profit
