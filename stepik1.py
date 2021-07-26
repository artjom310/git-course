n = int(input())
I = 0
II = 0
III = 0
IV = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 < y:
        I += 1
    elif x < 0 < y:
        II += 1
    elif x < 0 > y:
        III += 1
    elif x > 0 > y:
        IV += 1
print('Первая четверть:', I, '\n', 'Вторая четверть:', II, '\n',
'Третья четверть:', III, '\n', 'Четвертая четверть:', IV)
