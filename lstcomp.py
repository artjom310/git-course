'''Подсчет количества элементов
 в подсписках > среднего арф строки'''

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    arf = sum(a[i]) / len(a[i])
    k = 0
    for j in range(len(a)):
        if a[i][j] > arf:
            k += 1
    print(k)
