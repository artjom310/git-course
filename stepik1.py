a = [[1, 2, 3, 4],
     [5, 6, 3, 15],
     [0, 2, 3, 1],
     [5, 2, 8, 5]]
for i in range(len(a)):
    arf = sum(a[i]) / len(a[i])
    k = 0
    for j in range(len(a)):
        if a[i][j] > arf:
            k += 1
    print(k)

'''Подсчет количества элементов
 в подсписках > среднего арф строки'''
