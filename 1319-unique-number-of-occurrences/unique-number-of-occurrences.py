from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        size = len(arr)
        arr_counter = Counter(arr)
        print(arr_counter)
        distint_counts = Counter(arr_counter.values())
        print(distint_counts)
        results = set(distint_counts.values())

        return {1} == results