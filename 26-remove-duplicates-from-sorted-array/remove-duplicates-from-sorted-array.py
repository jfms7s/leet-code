class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1

        for index in range(1,len(nums)):
            if not nums[slow - 1] == nums[index]:
                nums[slow] = nums[index]
                slow = slow + 1
        return slow