def way_min(tuple_1, tuple_2):  # расчет расстояния между двух точек
    a = (tuple_2[0] - tuple_1[0]) ** 2
    b = (tuple_2[1] - tuple_1[1]) ** 2
    return (a + b) ** 0.5


print(way_min((0, 1), (1, 4)))
print(way_min((1, 4), (4, 1)) + way_min((0, 1), (1, 4)))

for i in range(10):
    print(i)
