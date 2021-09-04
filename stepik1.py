n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

b_i, b_j = 0, 0
max_v = matrix[0][0]
for i in range(len(matrix)):
    for j in range(m):
        if matrix[i][j] > max_v:
            max_v = matrix[i][j]
            b_i = i
            b_j = j
print(b_i, b_j)
'''6
8
-4 -3 -4 -4 -1 -8 -2 -3
-2 -3 -9 -7 -3 -4 -4 -5
-4 -3 -4 -4 -1 -2 -2 -3
-2 -3 -9 -3 -3 -1 -4 -5
-5 -3 -4 -4 -1 -2 -2 -3
-2 -3 -7 -8 -3 -4 -4 -5'''
