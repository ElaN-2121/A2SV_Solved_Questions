class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        count_1 = Counter(nums1)
        count_2 = Counter(nums2)

        for i in nums1:
            if count_2[i]>0 and i not in intersection:
                intersection.append(i)

        return intersection
