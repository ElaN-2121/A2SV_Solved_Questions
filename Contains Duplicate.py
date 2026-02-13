class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for num, freq in count.items():
            if freq>=2:
                return True
                break
        return False
