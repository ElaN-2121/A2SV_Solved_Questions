t  = int(input())
for _ in range(t):
    word = input()
    res = set()
    i = 0
    
    while i < len(word):
        j = i
        while j <len(word) and word[j] == word[i]:
            j+=1
        if (j-i) % 2 == 1:
            res.add(word[i])
        i = j
    print("".join(sorted(res)))
