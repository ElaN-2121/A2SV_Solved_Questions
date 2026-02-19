class Solution:
    def comparator(a,b):
        if int(a+b) >int(b+a):
            return -1
        elif int(a+b) < int(b+a):
            return 1
        else:
            return 0
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = list(map(str, nums))
        s_nums.sort(key=cmp_to_key(Solution.comparator))

        result=''.join(s_nums)
        if result[0] == "0":
            return "0"
        else:
            return result
    
