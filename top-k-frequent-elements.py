class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums=Counter(nums)
        return [num for num, freq in count_nums.most_common(k)]
