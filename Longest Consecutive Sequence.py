class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cons = 1
        cons = 1

        s_nums = list(set(nums))
        s_nums.sort()
        
        if not nums:
            return 0

        for i in range(len(s_nums)-1):
            
            if s_nums[i]+1 == s_nums[i + 1]:
                cons+=1
            else:
                max_cons = max(max_cons, cons)
                cons=1

        return max(max_cons, cons)


