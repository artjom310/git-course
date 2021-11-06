#  от i до вводимого числа цикл сделайте и append-ите по срезу[i::n]
'''import math

lst = list(input().split())
n = int(input())


def func_chunks_num(lst, c_num):
    n = math.ceil(len(lst) / c_num)

    for x in range(0, len(lst), n):
        e_c = lst[x:n + x:x+1]
        if len(e_c) &lt; n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c
print(list(func_chunks_num(lst, n)))
'''
kx, ky = input()
coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
kx = coor_j[kx]
ky = coor_i[ky]
matrix = [['.' for _ in range(8)] for _ in range(8)]
matrix[ky][kx] = 'Q'
for i in range(8):
    for j in range(8):
        if(i != ky or j != kx) and ((i == ky or j == kx) or (abs(i - ky) == abs(j - kx))):
            matrix[i][j] = '*'
for i in range(8):
    print(*matrix[i])
