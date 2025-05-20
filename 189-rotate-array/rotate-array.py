class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def invert(numbers,left,right):

            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

            return numbers
        size = len(nums)
        k = k % size
        invert(nums, size-k, size-1)
        invert(nums, 0 , size -k -1)
        return invert(nums, 0 , size -1)