n = int(input())
matrix = [[1] * n for _ in range(n)]

'''
1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1'''

for i in range(n):
    for j in range(n):
        if i > j and i < n-1-j or i < j and i > n-1-j:
            matrix[i][j] = 0

for i in matrix:
    print(*i)
