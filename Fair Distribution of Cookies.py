class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        '''
    Given:
        cookies array
        k: number of children
    Condition:
        No cookie bag split up
        unfairness = max candy by 1 child
        '''
    
        dist = [0] * k
        _max = float('inf')
        n= len(cookies)

        def backtrack(i):
            nonlocal _max
            if i == n:
                _max = min(_max, max(dist))
                return
            for child in range(k):
                dist[child] += cookies[i]
                if max(dist) < _max: 
                    backtrack(i + 1)
                dist[child] -= cookies[i]
                if dist[child] == 0:
                    break
            
        backtrack(0)
        return _max



