'''Поварачивает квадратную матрицу по часовой на 90'''
'''(i - 'номер строки') ** 2 + (j - 'номер столбца') ** 2 == 5
if abs(x1-x2) == 2 and abs(y1-y2) == 1 or abs(x1-x2) == 1 and abs(y1-y2) == 2'''  # валидность хода коня на доске  8х8

kx, ky = input()
coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
kx = coor_j[kx]
ky = coor_i[ky]
matrix = [['.' for _ in range(8)] for _ in range(8)]
matrix[ky][kx] = 'N'
for i in range(8):
    for j in range(8):
        if abs((kx-j) * (ky-i)) == 2:
            matrix[i][j] = '*'
for i in range(8):
    print(*matrix[i])
