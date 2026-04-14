len_arr, k =map(int, (input().split()))
arr = list(map(int, input().split()))

left = 0
current_sum = 0
ans = 0

for right in range(len_arr):
    current_sum += arr[right]
    
    while current_sum >= k:
        ans += len_arr - right
        current_sum -= arr[left]
        left += 1
print(ans)
    
