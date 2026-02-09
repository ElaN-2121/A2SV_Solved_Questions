class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(d) for i in nums for d in str(i)]
