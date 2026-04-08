class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: 
            return
        points.sort(key=lambda x: x[1])
        shot_pt = points[0][1]
        count_arrow = 1

        for start, end in points:
            if start<=shot_pt:
                continue
            else:
                shot_pt  = end
                count_arrow += 1
        
        return count_arrow
            



