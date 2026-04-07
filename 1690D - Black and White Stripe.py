t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    
    whites = s[:k].count('W')
    min_recolor = whites
    
    for i in range(k, n):
        if s[i] == 'W':
            whites += 1
        if s[i - k] == 'W':
            whites -= 1
        min_recolor = min(min_recolor, whites)

    print(min_recolor)
