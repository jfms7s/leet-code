class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        target_dict = dict()

        for pos in range(len(numbers)):
            value = numbers[pos]
            result = target_dict.get(value,None)

            if result is not None:
                return [result+1, pos+1]
            
            target_dict[target - value] = pos
