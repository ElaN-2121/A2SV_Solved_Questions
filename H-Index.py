class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        cited = 0
        
        for i, c in enumerate(citations):
            if c >= i + 1:
                cited = i + 1
            else:
                break
        return cited
