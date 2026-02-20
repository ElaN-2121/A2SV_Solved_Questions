class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        less = {}

        for i, num in enumerate(sorted_nums):
            if num not in less:
                less[num]=i

        return [less[num] for num in nums]
