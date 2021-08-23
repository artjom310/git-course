n = int(input())
a = []
for i in range(1, n + 1):
    i = [int(j)for j in range(1, i + 1)]
    a.append(i)
for i in a:
    print(i)
