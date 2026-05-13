class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                current = heappop(min_heap)
                heappush(min_heap, max(num, current))
        
        return min_heap[0]
