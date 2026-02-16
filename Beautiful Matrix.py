matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Center is at (2,2) in 0-based indexing
            print(abs(i - 2) + abs(j - 2))
