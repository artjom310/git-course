'''Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
'''
n, m = list(map(int, input().split()))
matrix = [[0] * m for _ in range(n)]
w = 1
for i in range(n + m):
    for j in range(min(i, m - 1), -1, -1):
        k = i - j
        if k < n:
            matrix[k][j] = w
            w += 1
for i in range(n):
    print(*matrix[i])
