post_dep_a = (0, 2)  # Почтовое отделение – (0, 2)
grib_st_b = (2, 5)  # Ул. Грибоедова, 104/25 – (2, 5)
big_sad_st_c = (6, 6)  # Ул. Большая Садовая, 302-бис
green_alley_d = (8, 3)  # Вечнозелёная Аллея, 742
bayker_st_e = (5, 2)  # Ул. Бейкер стрит, 221б


def way_min(tuple_1, tuple_2):  # расчет расстояния между двух точек
    a = (tuple_2[0] - tuple_1[0]) ** 2
    b = (tuple_2[1] - tuple_1[1]) ** 2
    return (a + b) ** 0.5


d_st = {1: '(0, 2)', 2: '(2, 5)', 3: '(6, 6)', 4: '(8, 3)', 5: '(5, 2)'}
graph = {}  # общий граф
graph[(0, 2)] = {}
graph[(0, 2)][(2, 5)] = way_min(post_dep_a, grib_st_b)
graph[(0, 2)][(6, 6)] = way_min(post_dep_a, big_sad_st_c)
graph[(0, 2)][(8, 3)] = way_min(post_dep_a, green_alley_d)
graph[(0, 2)][(5, 2)] = way_min(post_dep_a, bayker_st_e)

graph[(2, 5)] = {}  # графы по ребрам со значением расстояния
graph[(2, 5)][(0, 2)] = way_min(grib_st_b, post_dep_a)
graph[(2, 5)][(6, 6)] = way_min(grib_st_b, big_sad_st_c)
graph[(2, 5)][(8, 3)] = way_min(grib_st_b, green_alley_d)
graph[(2, 5)][(5, 2)] = way_min(grib_st_b, bayker_st_e)

graph[(6, 6)] = {}
graph[(6, 6)][(0, 2)] = way_min(post_dep_a, big_sad_st_c)
graph[(6, 6)][(2, 5)] = way_min(grib_st_b, big_sad_st_c)
graph[(6, 6)][(8, 3)] = way_min(big_sad_st_c, green_alley_d)
graph[(6, 6)][(5, 2)] = way_min(big_sad_st_c, bayker_st_e)

graph[(8, 3)] = {}
graph[(8, 3)][(0, 2)] = way_min(post_dep_a, green_alley_d)
graph[(8, 3)][(2, 5)] = way_min(grib_st_b, green_alley_d)
graph[(8, 3)][(6, 6)] = way_min(big_sad_st_c, green_alley_d)
graph[(8, 3)][(5, 2)] = way_min(green_alley_d, bayker_st_e)

graph[(5, 2)] = {}

towns = [
    [0, 3.605551275463989, 7.211102550927978, 8.06225774829855, 5.0],
    [3.605551275463989, 0, 4.123105625617661,
        6.324555320336759, 4.242640687119285],
    [7.211102550927978, 4.123105625617661, 0,
        3.605551275463989, 4.123105625617661],
    [8.06225774829855, 6.324555320336759, 3.605551275463989, 0, 3.1622776601683795],  # noqa
    [5.0, 4.242640687119285, 4.123105625617661, 3.1622776601683795, 0]
]

path = []
counter = 0
minPath = 1000
min_Counter = 0
res = []
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    if i1 != i2 and i1 != i3 and i1 != i4 and i1 != i5 and i2 != i3 and i2 != i4 and i2 != i5 and i3 != i4 and i3 != i5 and i4 != i5:  # noqa
                        path.append(
                            [(i1+1), (i2 + 1), (i3 + 1), (i4 + 1), (i5 + 1)])
                        # print(path)
                        if towns[i1][i2] + towns[i2][i3] + towns[i3][i4] + towns[i4][i5] < minPath:  # noqa
                            minPath = towns[i1][i2] + towns[i2][i3] + \
                                towns[i3][i4] + towns[i4][i5]
                            # print(towns[i1][i2], towns[i2][i3],
                                  # towns[i3][i4], towns[i4][i5])
                            # print(minPath)
                            minCounter = counter
                            res.append(towns[i1][i2])
                            res.append(towns[i2][i3])
                            res.append(towns[i3][i4])
                            res.append(towns[i4][i5])
                        counter += 1


if path[minCounter][-1] == 5:
    res.append(5.0)
elif path[minCounter][-1] == 4:
    res.append(8.06225774829855)
elif path[minCounter][-1] == 3:
    res.append(7.211102550927978)
else:
    res.append(3.605551275463989)

print(d_st[1], '->', d_st[2], res[0],
      d_st[3], res[0] + res[1],
      d_st[4], res[0] + res[1] + res[2],
      d_st[5], res[0] + res[1] + res[2] + res[3],
      d_st[1], '= ' + str(sum(res)))
