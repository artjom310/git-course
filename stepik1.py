#  Реализуйте функцию chunked(), которая принимает на вход список и число,
# задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.
s = input().split()
n = len(s) + 1
res = [[]]
for i in range(1, n):
    for j in range(n - i):
        res.append(s[j:j + i])
print(res)
