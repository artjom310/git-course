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


def check_latin_sq(m):
    N = len(m)
    row = []
    for i in range(N):
        row.append(set([]))
    cols = []
    for i in range(N):
        cols.append(set([]))
    
    inv = 0
    for i in range(N):
        for j in range(N):
            row[i].add(m[i][j])
            cols[j].add(m[i][j])
            if int(m[i][j]) > N or int(m[i][j]) <= 0:
                inv += 1
    
    n_row = 0
    n_cols = 0
    for i in range(N):
        if len(row[i]) != N:
            n_row += 1
        if len(cols[i]) != N:
            n_cols += 1
    
    if n_cols == 0 or n_row == 0 and inv == 0:
        print('YES')
    else:
        print('NO')
    return


check_latin_sq(matrix)
