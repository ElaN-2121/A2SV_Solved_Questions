class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        current_subarray = 0
        unique_elements = 0

        for right in range(len(nums)):
            # Add nums[right] into the window (count)
            if count[nums[right]] == 0:
                unique_elements += 1
            count[nums[right]] += 1

            # Shrinling the window if too many distinct
            while unique_elements > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    unique_elements -= 1
                left += 1

            # Every subarray ending at right contributes (right - left + 1)
            current_subarray += right - left + 1 

        return current_subarray
