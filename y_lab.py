import math
'''Почтовое отделение – (0, 2)
Ул. Грибоедова, 104/25 – (2, 5)
Ул. Бейкер стрит, 221б – (5, 2)
Ул. Большая Садовая, 302-бис – (6, 6)
Вечнозелёная Аллея, 742 – (8, 3)'''

post_dep_a = (0, 2)  # Почтовое отделение – (0, 2)
grib_st_b = (2, 5)  # Ул. Грибоедова, 104/25 – (2, 5)
big_sad_st_c = (6, 6)  # Ул. Большая Садовая, 302-бис
green_alley_d = (8, 3)  # Вечнозелёная Аллея, 742
bayker_st_e = (5, 2)  # Ул. Бейкер стрит, 221б

lst_of_st = [(0, 2), (2, 5), (6, 6), (8, 3), (5, 2), (0, 2)]


def way_min(tuple_1, tuple_2):  # расчет расстояния между двух точек
    a = (tuple_2[0] - tuple_1[0]) ** 2
    b = (tuple_2[1] - tuple_1[1]) ** 2
    return (a + b) ** 0.5


graph = {}  # общий граф
graph['A'] = {}
graph['A']['B'] = way_min(post_dep_a, grib_st_b)
graph['A']['C'] = way_min(post_dep_a, big_sad_st_c)
graph['A']['D'] = way_min(post_dep_a, green_alley_d)
graph['A']['E'] = way_min(post_dep_a, bayker_st_e)

graph['B'] = {}  # графы по ребрам со значением расстояния
graph['B']['A'] = way_min(grib_st_b, post_dep_a)
graph['B']['C'] = way_min(grib_st_b, big_sad_st_c)
graph['B']['D'] = way_min(grib_st_b, green_alley_d)
graph['B']['E'] = way_min(grib_st_b, bayker_st_e)

graph['C'] = {}
graph['C']['A'] = way_min(post_dep_a, big_sad_st_c)
graph['C']['B'] = way_min(grib_st_b, big_sad_st_c)
graph['C']['D'] = way_min(big_sad_st_c, green_alley_d)
graph['C']['E'] = way_min(big_sad_st_c, bayker_st_e)

graph['D'] = {}
graph['D']['A'] = way_min(post_dep_a, green_alley_d)
graph['D']['B'] = way_min(grib_st_b, green_alley_d)
graph['D']['C'] = way_min(big_sad_st_c, green_alley_d)
graph['D']['E'] = way_min(green_alley_d, bayker_st_e)

graph['E'] = {}

'''graph['E']['A'] = way_min(post_dep_a, bayker_st_e)
graph['E']['B'] = way_min(grib_st_b, bayker_st_e)
graph['E']['C'] = way_min(big_sad_st_c, bayker_st_e)
graph['E']['D'] = way_min(green_alley_d, bayker_st_e)'''
infinity = math.inf
costs = {}
costs['B'] = graph['B']['A']
costs['C'] = graph['C']['A']
costs['D'] = graph['D']['A']
costs['E'] = infinity

parents = {}
parents['B'] = 'A'
parents['C'] = 'A'
parents['D'] = 'A'
parents['E'] = None

processed = []


def find_low_cost_node(costs):
    low_cost = float('inf')
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = costs
            low_cost_node = node
    return low_cost_node


node = find_low_cost_node(costs)
while node is None:
    cost = costs[node]
    n_bors = graph[node]
    for n in n_bors.keys():
        new_cost = cost + n_bors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_low_cost_node
print(node)
