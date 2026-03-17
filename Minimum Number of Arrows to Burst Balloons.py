class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        current_position = points[0][1]
        for start, end in points:
            if start > current_position:
                arrows += 1
                current_position = end
        return arrows


