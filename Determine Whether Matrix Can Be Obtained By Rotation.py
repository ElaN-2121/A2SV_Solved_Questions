from typing import List

class Solution:
    def transpose(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat

    def rotate90(self, mat):
        self.transpose(mat)
        for row in mat:
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        return mat

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate90(mat)
        return False
