#  Напишите программу, которая возводит квадратную матрицу в mm-ую степень.

'''Sample Input 1:
3
1 2 1
3 3 3
1 2 1
5
Sample Output 1:
1666 2222 1666
3333 4443 3333
1666 2222 1666
'''
from copy import deepcopy
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())


def sqrt_matrix(matrix, matrix1):  # ф-ия умножения матрицы саму на себя т.е 2 степень
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                c[i][j] += matrix[i][r] * matrix1[r][j]
    return c


def pow_matrix(a, n):  # ф-ия копирует матрицу и вохвращает умножение на себя в цикле до n-1
    p = deepcopy(a)
    for _ in range(n - 1):
        p = sqrt_matrix(p, a)
    return p


res = pow_matrix(matrix, m)
for i in range(n):
    print(*res[i])
