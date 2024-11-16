class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        matrix = [
            [1] * i for i in range(1,numRows+1)
        ]
        
        for i in range(numRows - 1):
            next_row = i + 1
            for j in range(i):
                print(i,j)
                matrix[next_row][j+1] = matrix[i][j] + matrix[i][j+1]

        return matrix