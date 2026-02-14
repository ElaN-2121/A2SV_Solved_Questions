class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        original = []
        changed.sort()

        if len(changed) %2  != 0:
            return []

        for num in changed:
            if count[num] == 0:
                continue
            if count[2 * num] ==0:
                return []

            original.append(num)
            count[num] -= 1
            count[2 * num] -= 1

        return original
