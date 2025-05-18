class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        fast = 0
        size = len(nums)
        while fast < size:

            if not (nums[fast] == 0):
                nums[slow],nums[fast]  = nums[fast], nums[slow]
                
                slow += 1

            fast +=1