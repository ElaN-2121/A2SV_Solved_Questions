class Solution:
    def isHappy(self, n: int) -> bool:
        num=str(n)
        num_list=list(map(int, num))
        seen=set()
        while True:
            num_sum=sum([i**2 for i in num_list])

            if num_sum==1:
                return True
            if num_sum in seen:
                return False
            seen.add(num_sum)
            num_list = list(map(int, str(num_sum)))
