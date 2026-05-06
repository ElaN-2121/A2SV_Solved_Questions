class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        n = len(nums)
        used = [False] * n
        ans = []

        def backtrack():
            if len(permutation) == n:
                ans.append(permutation[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                permutation.append(nums[i])

                backtrack()
                permutation.pop()
                used[i] = False
        backtrack()
        return ans
