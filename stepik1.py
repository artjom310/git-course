'''words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])'''

n = int(input())
result = {}
res1 = {}
keys = []
values = []
for i in range(n):
    a = input().split()
    keys.append(a[1])
    values.append(a[0].strip())

result = dict(zip(keys, values))
res1 = dict(zip(values, keys))
m = input()
if result.get(m) is not None:
    print(result.get(m))
else:
    print(res1.get(m))
