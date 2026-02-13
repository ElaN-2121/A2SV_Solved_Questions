class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1=None
        num2=None

        count_num1=0
        count_num2=0

        for i in nums:
            if i==num1:
                count_num1+=1
            elif i==num2:
                count_num2+=1
            elif count_num1==0:
                num1=i
                count_num1=1
            elif count_num2==0:
                num2=i
                count_num2=1
            else:
                count_num1-=1
                count_num2-=1
        result=[]
        n=len(nums)
        for candidate in [num1, num2]:
            if candidate is not None and nums.count(candidate)> n//3:
                result.append(candidate)
        return result    
