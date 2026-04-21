class Solution: #kinda like cyclic sort
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for index, val in enumerate(nums):
            if val != index + 1:
                return index + 1
        return n+1
                
