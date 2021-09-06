'''Поварачивает квадратную матрицу по часовой на 90'''
n = int(input())
a = []
res = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in reversed(range(n)):
        print(a[j][i], end=' ')
    print()
