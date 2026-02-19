class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        most_common=Counter(nums).most_common(1)
        value_dom, frequency_dom = most_common[0]

        left_count=0
        n=len(nums)

        for i in range(n):
            if nums[i] == value_dom:
                left_count+=1
            
            right_count = frequency_dom - left_count
            if left_count * 2 > i+1 and right_count * 2 > n-i-1:
                return i
        return -1

