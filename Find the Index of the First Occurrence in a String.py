class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        span = len(needle)
        for i in range(len(haystack) - span+1):
            if haystack[i:i+span] == needle:
                return i
        return -1
