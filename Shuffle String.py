class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        char_list = [0]*len(s)
        for i, needed_index in enumerate(indices):
            char_list[needed_index]=s[i]
        return "".join(char_list)
