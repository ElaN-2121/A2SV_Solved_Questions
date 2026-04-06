class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)

    # Step 1: Build frequency using difference array
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

    # Step 2: Prefix sum to get actual frequencies
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq = freq[:n]  # trim to length n

    # Step 3: Sort both arrays
        nums.sort()
        freq.sort()

    # Step 4: Multiply and sum
        total = sum(a * b for a, b in zip(nums, freq)) % MOD
        return total
