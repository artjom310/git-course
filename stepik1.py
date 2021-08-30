#  Реализуйте функцию chunked(), которая принимает на вход список и число,
# задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.
lst = list(input().split())
n = 1
s = []

for i in range(0, len(lst)):
    s += [lst[x:n + x] for x in range(0, len(lst), n)]
    n += 1
s.append([])
print(sorted(s, key=len))
