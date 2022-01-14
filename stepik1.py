'''
Телефонная книга
dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))'''

d = {}
for i in range(int(input())):
    a = input().lower().split()
    d.setdefault(a[1], []).append(a[0])
lst = []
for i in range(int(input())):
    b = input().lower()
    lst.append(b)
for i in lst:
    try:
        print(*d.get(i))
    except:
        print('абонент не найден')
