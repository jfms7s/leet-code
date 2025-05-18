class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix = [1] * size
        sufix = [1] * size

        for i in range(1,size):
            prefix[i] = prefix[i-1] * nums[i-1]


        for i in range(size-2,-1,-1):
            sufix[i] = sufix[i+1] * nums[i+1]

        return [
            prefix[i] * sufix[i]
            for i in range(size)
        ]