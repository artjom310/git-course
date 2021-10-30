#  Doc_str там решение которое в принципе понял.
'''for i in range(n):
    for j in range(k):
        for r in range(m):
            C[i][j] += matrix[i][r] * matrix1[r][j]'''

import numpy as np
n, m = map(int, input().split())

matrix = [[int(i) for i in input().split()] for _ in range(n)]
input()

m, k = list(map(int, input().split()))
matrix1 = [[int(i) for i in input().split()] for _ in range(m)]
a = np.matrix(matrix)
b = np.matrix(matrix1)
c = a * b

for i in c.tolist():
    print(*i)
