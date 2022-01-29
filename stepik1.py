'''Sample Input 1:

*!*!*?
3
а: 3
н: 2
с: 1
'''
a = input()
n = int(input())
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
# print(d)  # {'*': 3, '!': 2, '?': 1}

d1 = {}

keys = []
values = []
for i in range(n):
    i = input().split(': ')
    keys.append(int(i[1]))
    values.append(i[0])
d1 = dict(zip(keys, values))  # {'3': 'а', '2': 'н', '1': 'с'}
# print(d1)
s = []
for i in a:
    s.append(d1.get(d.get(i)))
print(''.join(s))
