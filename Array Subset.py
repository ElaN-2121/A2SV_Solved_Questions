from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        return Counter(b)<=Counter(a)
    
