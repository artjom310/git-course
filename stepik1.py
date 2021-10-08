n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1
    print(*matrix[i])
