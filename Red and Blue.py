t = int(input())
for _ in range(t):
    input()
    r = list(map(int, input().split()))
    input()
    b = list(map(int, input().split()))
    
    def max_prefix(arr):
        s = 0
        best = 0
        for x in arr:
            s += x
            best = max(best, s)
        return best
    
    print(max_prefix(r) + max_prefix(b))
