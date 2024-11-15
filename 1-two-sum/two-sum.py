class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()

        for (current,number) in enumerate(nums):
            expected_value = target - number
            previous = index.get(expected_value,None)
            index[number]=current
            
            if(previous is not None):
                return [previous,current]

            