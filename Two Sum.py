class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[(index, value) for index, value in enumerate(nums)]
        arr.sort(key=lambda x:x[1])

        left=0
        right=len(arr)-1
        while left<right:
            mid=arr[left][1] + arr[right][1]

            if mid==target:
                return ([arr[left][0], arr[right][0]])
            elif mid<target:
                left+=1
            else:
                right-=1
