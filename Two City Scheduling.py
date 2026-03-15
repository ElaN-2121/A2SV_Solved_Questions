from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sorting by difference between costA and costB
        costs.sort(key=lambda x: x[0] - x[1])
        
        half = len(costs) // 2
        total = 0
        
        # First half → city A, second half → city B
        for i in range(half):
            total += costs[i][0]  # city A
        for i in range(half, 2*half):
            total += costs[i][1]  # city B
        
        return total
