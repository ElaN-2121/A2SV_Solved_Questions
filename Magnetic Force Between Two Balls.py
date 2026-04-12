class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
        def canPlace(d):
            count, last = 1, position[0]
            for p in position[1:]:
                if p - last >= d:
                    count += 1
                    last = p
                    if count >= m:
                        return True
            return False
    
        left, right = 1, position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
