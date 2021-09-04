#  алгоритм проверяет симметричная ли квадратная матрица
#  относительно главной диагонали
#  выводит да или нет
n = int(input())
a = []
res = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(len(a[i])):
        if i != j:
            if a[i][j] == a[j][i]:
                res.append('YES')
            else:
                res.append('NO')
if 'NO' in res:
    print('NO')
else:
    print('YES')
