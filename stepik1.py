#  Поменять местами столбы матрицы
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
i, j = list(map(int, input().split()))

for c in range(len(matrix)):
    matrix[c][i], matrix[c][j] = matrix[c][j], matrix[c][i]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
