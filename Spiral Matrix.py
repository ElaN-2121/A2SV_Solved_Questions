class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        result = []

        while left <= right and top <= bottom:
            #Moving to right
            for e in range(left, right+1):
                result.append(matrix[top][e])
            top += 1

            #Moving down
            for n in range(top, bottom+1):
                result.append(matrix[n][right])
            right -= 1

            if top <= bottom:
                #moving left
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
                bottom-=1
            if left <= right:
                # Move up 
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
