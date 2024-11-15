class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for index in range(1,len(nums)):
            if not nums[slow] == nums[index]:
                slow = slow + 1
                nums[slow] = nums[index]
        return slow +1