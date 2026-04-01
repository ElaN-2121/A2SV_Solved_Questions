class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
    
    # Step 1: Build difference array
        for start, end, direction in shifts:
            if direction == 1:  # forward
                diff[start] += 1
                diff[end + 1] -= 1
            else:  # backward
                diff[start] -= 1
                diff[end + 1] += 1
    
    # Step 2: Prefix sum to get actual shifts
        for i in range(1, n):
            diff[i] += diff[i - 1]
    
    # Step 3: Build result string
        res = []
        for i in range(n):
            shift = diff[i] % 26  # reduce large shifts
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(new_char + ord('a')))
    
        return "".join(res)
        
