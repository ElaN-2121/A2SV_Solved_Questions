arr_len, max_sum = map(int, input().split())
arr = list(map(int, input().split()))
    
left = 0
current_sum = 0
ans = 0

for right in range(arr_len):
    current_sum += arr[right]
    
    while current_sum > max_sum:
        current_sum -= arr[left]
        left += 1
        
    ans += right - left + 1

print(ans)
            
