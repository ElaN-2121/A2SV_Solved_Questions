class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:  
        common_word=[]
        min_index=float('inf')
        list1_index={}
        list2_index={}
        for i in range(len(list1)):
            list1_index[list1[i]]=i

        for j in range(len(list2)):
            list2_index[list2[j]]=j

        for word, index in list1_index.items():
            if word in list2_index:
                total=list2_index[word]+index
                if total <min_index:
                    common_word=[word]
                    min_index=total
                elif total==min_index:
                    common_word.append(word)
        return common_word
       
