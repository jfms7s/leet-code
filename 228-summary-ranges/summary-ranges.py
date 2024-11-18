
def rangeToString(min_range,max_range):

    if min_range == max_range:
        return f"{min_range}"
    else:
        return f"{min_range}->{max_range}"

class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []

        result = []

        index,size = 0,len(nums)
        current_value = nums[index]

        min_index = 0
        while (index:=index+1) < size:
            print(nums[index-1],nums[index])
            if not (nums[index-1] == nums[index]-1):
                result.append(rangeToString(nums[min_index],nums[index-1]))
                min_index=index

        result.append(rangeToString(nums[min_index],nums[index-1]))


        return result
