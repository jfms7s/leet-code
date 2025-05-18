class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_value = max(candies)

        return [
            (i + extraCandies) >= max_value
            for i in candies
        ]
