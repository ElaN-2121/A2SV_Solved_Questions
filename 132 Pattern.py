class Solution:
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')  # a candidate for nums[k]
        
        # Travering from right to left
        for num in reversed(nums):
            if num < third:
                return True  # nums[i] < nums[k] < nums[j]
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)
        
        return False
