from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find index of max element in arr[:size]
            max_index = arr.index(max(arr[:size]))

            # If it's already in the correct position, skip
            if max_index == size - 1:
                continue

            # Bring max to front if not already
            if max_index != 0:
                res.append(max_index + 1)
                arr[:max_index + 1] = list(reversed(arr[:max_index + 1]))

            # Move max to its correct position
            res.append(size)
            arr[:size] = list(reversed(arr[:size]))

        return res
