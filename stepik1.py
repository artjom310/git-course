#  Реализуйте функцию chunked(), которая принимает на вход список и число,
# задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.
lst = list(input().split())
n = int(input())


def chunked(lst, n):
    return [lst[x:n + x] for x in range(0, len(lst), n)]


print(chunked(lst, n))
