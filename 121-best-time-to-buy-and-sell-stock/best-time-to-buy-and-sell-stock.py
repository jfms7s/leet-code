class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value_min = prices[0]
        profit = 0

        for value in prices:
            profit = max(profit, value - value_min)
            value_min = min(value, value_min)

        return profit