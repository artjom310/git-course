'''Проверить чтобы все отсортированные строки матрицы были равны 
list(range(1, n+1))
Транспонировать матрицу
Пункт первый
Вывод YES если <пункт 1> and <пункт 3> иначе NO
Sample Input 1:
4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:
YES
'''
n = int(input())
matrix = [input().split() for _ in range(n)]
c = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = c[j][i]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if c[i][j] not in matrix[i] and c[i][j] not in c[i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)
