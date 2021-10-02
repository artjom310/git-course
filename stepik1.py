'''На вход программе подаются два натуральных числа nn и mm. Напишите программу, 
которая создает матрицу размером n на mn×m и 
заполняет её числами от 1 до n * m в соответствии с образцом.'''


n, m = list(map(int, input().split()))

matrix = []
g = m
a = 1
for i in range(n):
    matrix.append(list(range(a, g + 1)))
    a = g + 1
    g += m
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
