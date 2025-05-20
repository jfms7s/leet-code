class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        vindex = dict()
        size = len(grid)
        result = 0

        for i in range(size):

            key = tuple(grid[j][i] for j in range(size))
            vindex[key] = vindex.get(key,0) + 1


        for el in grid:
            key = tuple(el)
            if key in vindex:
                result += vindex[key]

        return result