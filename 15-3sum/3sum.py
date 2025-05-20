class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        size = len(nums)
        nums = sorted(nums)

        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            index = dict()
            for j in range(i+1,size):

                pairs = index.get(nums[j], None)
                
                if pairs:
                    
                    a,b = pairs
                    results.add((a,b,nums[j]))
                else:
                    index[-(nums[i] + nums[j]) ] = [nums[i], nums[j]]

        return list(results)