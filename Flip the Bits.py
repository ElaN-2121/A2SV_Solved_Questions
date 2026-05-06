t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    count_ones = 0
    count_zeros = 0
    balanced = [False] * n
    
    for i in range(n):
        if a[i] == "1":
            count_ones+=1
        else:
            count_zeros +=1
        if count_ones == count_zeros:
            balanced[i] = True
    flip = False
    possible = True
    for i in range(n-1, -1, -1):
        curr_a = a[i]
        if flip:
            curr_a = "1" if a[i]=="0" else "0"
            
        if curr_a != b[i]:
            if not balance[i]:
                possible = False
                break
            flip = not flip
                
    print("YES" if possible else "NO")

            
