class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        for response in responses:
            for chosen_response in set(response):
                count[chosen_response] += 1
        common = ""
        max_occur = 0
        for word, freq in count.items():
            if freq > max_occur or (freq == max_occur and word < common):
                common = word
                max_occur = freq
        return common 
