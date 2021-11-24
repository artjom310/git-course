# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
n = int(input())
lst = []
for i in range(n):
    s = input()
    s = s.lower()
    lst.append(set(s))
for i in lst:
    print(len(i))
