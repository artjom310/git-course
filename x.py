points = [(-1, 1), (5, 6), (12, 0),
          (4, 3), (0, 1), (-3, 2),
          (0, 0), (-1, 3), (2, 0),
          (3, 0), (-9, 1), (3, 6), 
          (8, 8)
          ]


def comparator(item):  # ф-ия считает среднее ареф-е в кортеже
    c = 0
    arf = len(item)
    for i in item:
        c += i
    return c / arf


print(min(points, key=comparator))
print(max(points, key=comparator))
