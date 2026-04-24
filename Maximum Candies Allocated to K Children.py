class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def can(mid):
            if mid == 0:
                return True
            else:
                return (sum(c//mid for c in candies) >= k)

        ans = 0
        left = 1
        right = max(candies)

        while left <= right:
            mid = (left + right) //2 
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
