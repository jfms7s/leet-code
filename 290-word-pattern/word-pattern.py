from itertools import zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        split_s = s.split()
        pset = set(pattern)
        sset = set(split_s)
        zip_set = set(zip_longest(pattern, split_s, fillvalue=""))
        print((pset) , (sset) , (zip_set))
        return len(pset) == len(sset) == len(zip_set)