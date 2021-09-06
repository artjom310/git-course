'''Поменять местами главную и побочную диаггонали'''
n = int(input())
a = []
res = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    a[i][i], a[n-i-1][i] = a[n-i-1][i], a[i][i]
print()
for i in a:
    print(*i)
