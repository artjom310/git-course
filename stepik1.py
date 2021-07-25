# print('{:,}'.format(int(input())))
a = 0
n = int(input())  # сколько всего солдат в кругу
k = int(input())  # очередность, каждый k солдат умирает
for i in range(1, n + 1):
    a = (a + k) % i
print(a + 1)
