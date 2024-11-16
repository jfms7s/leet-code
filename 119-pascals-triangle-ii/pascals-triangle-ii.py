class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        result = [1] * rowIndex

        for i in range(2,rowIndex):
            for j in reversed(range(1,i)):
                result[j] = result[j-1] + result[j]
        return result