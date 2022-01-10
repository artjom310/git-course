'''На вход программе подаются два предложения.
Напишите программу, которая определяет, являются они анаграммами или нет.
Ваша программа должна игнорировать регистр символов,
знаки препинания и пробелы.'''


#  re.sub(u'[^\w\d\s]+', '', str())   words = re.sub(r'[.,;:-?-!]', '', input())
a = [i.strip('.,!?:;-') for i in input().lower().strip()]
b = [i.strip('.,!?:;-') for i in input().lower().strip()]
# rint(a, b, sep='\n')
d = {}
d1 = {}
for i in a:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
    else:
        continue

for i in b:
    if i.isalpha():
        d1[i] = d1.get(i, 0) + 1
    else:
        continue

if d == d1:
    print("YES")
else:
    print('NO')
# print(d, d1, sep='\n')
