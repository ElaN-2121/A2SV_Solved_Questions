class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_num=Counter(nums)
        return [i for i in count_num if count_num[i] >= 2] 
