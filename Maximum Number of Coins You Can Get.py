class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()

        left = 0
        right = len(piles) - 1
        me = 0

        for _ in range(n):

            right-=1
            me += piles[right]
            right -= 1
            left += 1

        return me
