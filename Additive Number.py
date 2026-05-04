class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def valid_number(s: str) -> bool:
            return not (len(s) > 1 and s[0] == "0")
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                first, second = num[:i], num[i:j]
                if not valid_number(first) or not valid_number(second):
                    continue
                a, b = int(first), int(second)
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c
                if k == n:
                    return True
        return False

