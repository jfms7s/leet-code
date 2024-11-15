class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""


        sizes = [len(sub_list) for sub_list in strs]
        min_size = min(sizes)

        for index in range(min_size):
            
            for string in strs:
                if string[index] != strs[0][index]:
                    return string[0:index]

        return strs[0][0:min_size]

            