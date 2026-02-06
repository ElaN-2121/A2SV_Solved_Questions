class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #Brute Force Approach
        """
        for num in range(left, right+1):
            isCovered=False
            for start, end in ranges:
                if start<= num and num <=end:
                    isCovered=True
                    break
            if isCovered==False:
                return False
        return True
        """
        covered_array=[0]*52

        for start, end in ranges:#initializing the start and end value of range inside the array
            covered_array[start]+=1
            if end+1 < len(covered_array):
                covered_array[end+1]-=1

        for i in range(1, len(covered_array)):# using prefix sum to check coverage
            covered_array[i]+=covered_array[i-1]
        for num in range(left, right+1):# checking if left and right range exists
            if covered_array[num]<=0:
                return False
        return True 
