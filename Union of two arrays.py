class Solution:    
    def findUnion(self, a, b):
        c=set(a).union(set(b))
        return list(c)
