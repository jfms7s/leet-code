class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix = [1] * size
        sufix = [1] * size
        result = [1] * size

        previous_result = 1
        for i in range(size):
            prefix[i] = previous_result
            previous_result = nums[i] * previous_result

        previous_result = 1
        for i in range(size-1,-1,-1):
            sufix[i] = previous_result
            previous_result = previous_result * nums[i]

        for i in range(size):
            result[i] = prefix[i] * sufix[i]

        return result