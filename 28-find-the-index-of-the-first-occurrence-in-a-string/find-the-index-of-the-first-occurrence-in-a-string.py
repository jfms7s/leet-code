class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_size = len(needle)
        haystack_size = len(haystack)
        if needle_size > haystack_size:
            return -1

        for index in range(haystack_size):
            end_index = index + needle_size
            if end_index > haystack_size: 
                return -1

            if haystack[index:end_index] == needle:
                return index
        return -1
