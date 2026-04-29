class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(start, prev, count):
            if start == len(s):
                return count >= 2  
            num = 0
            for i in range(start, len(s)):
                num = num * 10 + int(s[i])
                if prev is None or num == prev - 1:
                    if dfs(i + 1, num, count + 1):
                        return True
                if prev is not None and num >= prev:
                    break  # no need to continue if not descending
            return False
        
        return dfs(0, None, 0)
