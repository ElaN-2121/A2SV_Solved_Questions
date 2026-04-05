class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # base case: empty prefix
    
        curr_sum = 0
        result = 0
    
        for num in nums:
            curr_sum += num
        # check if there's a prefix that makes sum = goal
            result += prefix_count[curr_sum - goal]
        # record current prefix sum
            prefix_count[curr_sum] += 1
    
        return result
