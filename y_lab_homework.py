'''
qergqerg
'''
P = 'numbers.txt'

#p = 'grades.txt'

with open(P, 'r', encoding='utf-8') as file:
    d = {}
    for i in file:
        i = i.split()
        d[i[0]] = i[1::]
    C = 0
    for k, v in d.items():
        v = list(map(int, v))
        if v[0] >= 65 and v[1] >= 65 and v[2] >= 65:
            C += 1
    print(C)
