class Solution:
    def isPalindrome(self, x: int) -> bool:
        listx=list(str(x))
        return listx==listx[::-1]
