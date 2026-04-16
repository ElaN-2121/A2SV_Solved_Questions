from collections import Counter

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    sock = list(map(int, input().split()))
    
    left = sock[:l]
    right = sock[l:]
    
    left_color = Counter(left)
    right_color = Counter(right)

    # Remove matching pairs
    for i in left_color:
        common = min(left_color[i], right_color[i])
        left_color[i] -= common
        right_color[i] -= common

    left_total = sum(left_color.values())
    right_total = sum(right_color.values())

    cost = 0

    # Ensure right side is larger
    if left_total > right_total:
        left_color, right_color = right_color, left_color
        left_total, right_total = right_total, left_total

    # Use same-color pairs
    for color in right_color:
        while right_total - left_total > 1 and right_color[color] >= 2:
            right_color[color] -= 2
            right_total -= 2
            cost += 1

    # Balance sides
    diff = (right_total - left_total) // 2
    cost += diff
    left_total += diff
    right_total -= diff

    # Final pairing
    cost += left_total

    print(cost)
