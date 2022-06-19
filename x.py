def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def func_apply(fn, item):
    return list(map(fn, item))


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))

'''[7, 14, 21, 28, 35, 42]
[4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6']
'''