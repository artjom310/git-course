import numpy as np

n, m = list(map(int, input().split()))
matrix = []
g = m
a = 1
for i in range(n):
    matrix.append(list(range(a, g + 1)))
    a = g + 1
    g += m


def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp+[matr[i][j]]
        res = res+[tmp]
    return res


tr_matrix = transpose(matrix)
m1 = np.array(tr_matrix)
m_res = np.reshape(m1, (n, m), order='F')
for i in m_res:
    print(*i)
print()
