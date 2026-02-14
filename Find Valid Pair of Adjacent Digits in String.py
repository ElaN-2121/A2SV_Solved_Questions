class Solution:
    def findValidPair(self, s: str) -> str:
        count=Counter(s)
        valid_pair=""
        
        for i in range(len(s)-1):
            if s[i] != s[i+1] and (count[s[i]]==int(s[i]) and count[s[i+1]]==int(s[i+1])):
                return s[i:i+2]
        return ""
