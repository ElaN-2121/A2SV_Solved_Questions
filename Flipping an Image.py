class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        left = 0
        for i in image:
            left = 0
            right = len(i)-1
            while left < right:
                i[left], i[right] = i[right], i[left]
                left += 1
                right -= 1
        for i in image:
            for num in range(len(i)):
                if i[num]==1:
                    i[num] = 0
                else:
                    i[num] = 1
        return image
