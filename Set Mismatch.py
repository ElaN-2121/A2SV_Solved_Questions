class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        duplicate = 0
        missing = 0

        for i in nums:
            if i in seen:
                duplicate = i
            seen.add(i)
        
        for j in range(len(nums)+1):
            if j not in seen:
                missing = j
        
        return ([duplicate, missing])
