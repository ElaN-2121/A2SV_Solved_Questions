class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter = 0

        for i in range(len(nums)-1,1,-1):
            if nums[i-1] + nums[i-2] > nums[i]:
                max_perimeter = nums[i-1] + nums[i-2] + nums[i] 
                break

        return max_perimeter
