class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1 or len(nums) == len(set(nums)):
            return False

        resuts=dict()

        for i,current in enumerate(nums):
            prev = resuts.get(current, None)
            
            if prev is not None and i-prev <= k:
                return True

            resuts[current] = i
        return False



