from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    answer = float("inf")

    for length in range(2, 8):
        for i in range(n - length + 1):
            sub = s[i:i+length]
            c = Counter(sub)

            if c['a'] > c['b'] and c['a'] > c['c']:
                answer = length
                break
        
        if answer != float("inf"):
            break
    
    print(answer if answer != float("inf") else -1)
