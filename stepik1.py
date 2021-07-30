import timeit


import re
lst = []
pregex = ''.join(f'.*?{i}' for i in 'anton')
for i in range(int(input())):
    if re.search(pregex, input()):
        lst.append(i)
for i in range(1, len(lst) + 1):
    print(i)
