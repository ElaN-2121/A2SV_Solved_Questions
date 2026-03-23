n = int(input())
points = list(map(int, input().split()))

points.sort()

# If n is odd, n//2 gives middle element
# If n is even, n//2 - 1 gives left median
median = points[(n - 1) // 2]

print(median)
