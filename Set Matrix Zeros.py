class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        set_col = set()
        set_row = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_col.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in set_row or j in set_col:
                    matrix[i][j] = 0
                
            
