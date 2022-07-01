from functools import reduce 

'''
преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
находит произведение чисел из списка numbers.
'''

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and name[::-1] == name , words))
reduce_result = reduce(lambda x, y: x * y, numbers, 1)


print(map_result)
print(filter_result)
print(reduce_result)