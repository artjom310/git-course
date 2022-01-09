'''{'Змея': ' язык программирования Python',
'Баг': ' от англ. bug — жучок, клоп, ошибка в программе',
'Конфа': ' конференция',
'Костыль': ' код, который нужен, чтобы исправить несовершенство ранее написанного кода',
'Бета': ' бета-версия, приложение на стадии публичного тестирования'}

'''

n = int(input())
result = {}
keys = []
values = []
for i in range(n):
    a = input().split(':')
    keys.append(a[0].lower())
    values.append(a[1].strip())

result = dict(zip(keys, values))
m = int(input())
ans = []
for i in range(m):
    d = input().lower()
    ans.append((result.get(d, 'Не найдено')))

for i in ans:
    print(i)
