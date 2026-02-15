class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        transpose = []

        for j in range(col):
            new_matrix = []

            for i in range(row):
                new_matrix.append(matrix[i][j])
            transpose.append(new_matrix)

        return transpose
