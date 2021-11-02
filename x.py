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
#  Симметричная матрица относительн побочной диагонали
n = int(input())
matrix = [input().split() for _ in range(n)]
c = []
for stroka in matrix:
    stroka.reverse()
    c.append(stroka)
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if c[i][j] != c[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)
