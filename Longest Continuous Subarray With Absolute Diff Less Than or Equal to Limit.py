class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_length = 0
        left = 0
        max_dequeue = deque()
        min_dequeue = deque()

        for right in range(len(nums)):
            while max_dequeue and nums[right] > max_dequeue[-1]:
                max_dequeue.pop()
            max_dequeue.append(nums[right])

            while min_dequeue and nums[right] < min_dequeue[-1]:
                min_dequeue.pop()
            min_dequeue.append(nums[right])

            while max_dequeue[0] - min_dequeue[0] > limit:
                if nums[left] == max_dequeue[0]:
                    max_dequeue.popleft()
                if nums[left] == min_dequeue[0]:
                    min_dequeue.popleft()
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length
