arr1_len, arr2_len = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
    
left1 = 0
left2 = 0
ans = 0
    
while ( left1 < arr1_len ) and ( left2 < arr2_len ):
    if arr1[left1] < arr2[left2]:
        left1 += 1
    elif arr1[left1] > arr2[left2]:
        left2 += 1
    else:
        val = arr1[left1]
        count1 = 0
        count2 = 0
            
        while left1 <arr1_len and arr1[left1] == val:
            left1 += 1
            count1 += 1
        while left2 < arr2_len and arr2[left2] == val:
            left2 += 1
            count2 += 1
            
        ans += count1*count2
    
print(ans)
            
