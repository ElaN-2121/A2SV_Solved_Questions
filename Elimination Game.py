class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:
            if left or remaining% 2 != 0: # even = head stays, odd = head moves
                head += step

            remaining //= 2
            step *= 2
            left = not left

        return head

        
