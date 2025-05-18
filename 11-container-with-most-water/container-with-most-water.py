class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:

            current_height = min(height[left], height[right])
            max_area = max(max_area, (right - left) * current_height )

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area