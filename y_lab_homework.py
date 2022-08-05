'''
Вывод списка строк в обратном порядке.
'''
p = 'numbers.txt'

with open(p, encoding='utf-8') as f:
    for i in reversed(f.readlines()):
        print(i.strip())
