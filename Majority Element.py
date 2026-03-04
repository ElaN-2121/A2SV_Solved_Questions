class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = None
        num2 = None

        count_1 = 0
        count_2 = 0

        for num in nums:
            if num1 ==None:
                num1 = num
            elif num2 == None:
                num2 = num
            elif count_1 == 0:
                num1 = num
                count_1 += 1
            elif count_2 == 0:
                num2 = num
                count_2 += 1
            elif num == num1:
                count_1 += 1
            elif num == num2:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        result = []
        n = len(nums)
        for candidate in [num1, num2]:
            if candidate is not None and nums.count(candidate)>n//3:
                result.append(candidate)

        return result    
