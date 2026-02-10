class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference= strs[0]

        if not strs:
            return ""

        if len(strs)==1:
            return strs[0]

        prefix=""

        for i in range(len(reference)):
            for s in strs:
                if len(s)<=i or s[i]!=reference[i]:
                    return prefix 
                    break
            prefix+=reference[i]
        return prefix
