m = int(input())  # строки в матрице
n = int(input())  # столбы в матрице \ другим словом подсписок
s = [[0] * n for i in range(m)]  # заполнение матрицы 0
for i in range(m):
    for j in range(n):
        s[i][j] = input()  # замена элемнтов матрицы
for row in s:
    print(' '.join(list(map(str, row))))  # перебор матрицы и вывод построчно
