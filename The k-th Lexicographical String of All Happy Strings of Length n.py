class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
    
        def dfs(path):
            if len(path) == n:
                res.append(path)
                return
            for ch in 'abc':
                if not path or path[-1] != ch:
                    dfs(path + ch)
    
        dfs("")
        return res[k-1] if k <= len(res) else ""
