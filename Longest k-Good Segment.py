from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
freq = defaultdict(int)
longest = 0
best_pair = (0,0)

for right in range(n):
    freq[arr[right]] += 1
    
    while len(freq)>k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]
        left +=1
    if (right - left + 1) > longest:
        best_pair = (left, right)
        longest = right -left + 1
        
print(best_pair[0] + 1, best_pair[1] + 1)
