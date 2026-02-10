class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars=Counter(chars)
        can_be_formed=0
        for word in words:
            if Counter(word) <= count_chars:
                can_be_formed+=len(word)
        return can_be_formed
