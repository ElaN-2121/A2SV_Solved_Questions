class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count_n=0
        for i in grid:
            for j in range(len(i)):
                if i[j]<0:
                    count_n+=len(i)-j
                    break
        return count_n
