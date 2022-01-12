'''2
d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    d.update(dict.fromkeys(cities, country))
for _ in range(int(input())):    
    print(d[input()])
'''


n = int(input())
keys = []
values = []
for i in range(n):
    a = input().split()
    keys.append(a[0])
    values.append(a[1:])
d = {}
for i in range(len(keys)):
    a = d.fromkeys(values[i], keys[i])
    d.update(a)
m = int(input())
b = []
for i in range(m):
    b.append(input().strip())
for i in b:
    print(d.get(i))
