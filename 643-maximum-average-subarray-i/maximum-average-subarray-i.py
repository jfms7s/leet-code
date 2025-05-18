class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        size = len(nums)
        
        acc = sum(nums[left:right])
        avg = acc/k

        while right < size:
            acc = acc - nums[left] + nums[right]
            avg = max(avg, acc/k)

            left += 1
            right += 1
            

        return avg