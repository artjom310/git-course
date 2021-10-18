'''Sample Input 1:

5 5
Sample Output 1:

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4'''


n, m = list(map(int, input().split()))
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
for i in matrix:
    print(*i)
