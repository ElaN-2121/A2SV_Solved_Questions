class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for cell in matrix:
            left=0
            right=len(cell)-1
            while left<right:
                cell[left], cell[right] = cell[right], cell[left]
                left += 1
                right -= 1
            
        
        
