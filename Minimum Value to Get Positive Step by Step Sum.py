from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_sum = float('inf')

        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)

        # If min_sum is already >= 1, we only need startValue = 1
        return 1 if min_sum >= 1 else 1 - min_sum
