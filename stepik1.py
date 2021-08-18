import re

lst = {x: input() for x in range(1, int(input()) + 1)}
print(lst)
regex = ''.join(f'.*?{i}' for i in 'anton')
a = []
for k, v in lst.items():
    if re.search(regex, v):
        a.append(k)
print(*a)
