class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total_operations = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            total_operations += 1
        # If no doubles left, we just subtract down to 1 in one step
        return total_operations + (target - 1)
