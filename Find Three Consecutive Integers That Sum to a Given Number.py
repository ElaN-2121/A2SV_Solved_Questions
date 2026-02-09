class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        numd= num-3
        n= numd//3
        if (3*n+3)==num:
            return [n, n+1, n+2]
        else:
            return []
