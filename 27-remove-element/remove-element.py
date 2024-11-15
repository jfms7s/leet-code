class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        slow = 0

        for i in range(len(nums)):
            
            nums[slow] = nums[i]

            if not nums[i] == val:
                slow += 1

        return slow