from functools import reduce


def product_of_odds(*data):
    '''ф-ия перемножает нечетные числа'''
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2, data), 1)

print(product_of_odds(1,2,3,4,5))
