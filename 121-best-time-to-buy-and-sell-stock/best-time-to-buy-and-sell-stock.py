class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value_min = prices[0]
        value_max = prices[0]
        profit = 0


        for value in prices:

            if value_min > value:
                value_min = value
            else:
                profit = max(profit, value - value_min)

        return profit