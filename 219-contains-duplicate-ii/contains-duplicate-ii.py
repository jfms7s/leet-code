class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        resuts=dict()

        for i in range(len(nums)):
            current = nums[i]
            prev = resuts.get(current, None)
            
            if prev is not None and abs(i-prev) <= k:
                return True

            resuts[current] = i
        return False



