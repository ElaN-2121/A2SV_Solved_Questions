class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            remainder = remainder if remainder >= 0 else remainder + k
            result += count[remainder]
            count[remainder] += 1
        return result
