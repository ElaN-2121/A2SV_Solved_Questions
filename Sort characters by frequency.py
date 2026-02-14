class Solution:
    def frequencySort(self, s: str) -> str:
        _list = list(s)
        count = Counter(_list)

        _decreasing_store = count.most_common()
        word = ""
        for char,freq in _decreasing_store:
            word += char * freq
        return word
