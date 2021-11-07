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

n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1+f2+f3
