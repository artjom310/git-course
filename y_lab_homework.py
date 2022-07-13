ph = 'numbers.txt'
s = '''
телефон	4	12500
бургер	1	500
курс	1	1400
подписка	40	9500
наушники	2	22450
телефон	2	2500
ноутбук	5	155000
диван	100	300
'''
with open(ph, 'r', encoding='utf-8') as f:
    
    '''a = f.readline()
    new_str = '\n'.join(el.strip() for el in a.split('\n') if el.strip())
    lst = new_str.split()
    print(lst)'''
    c = 0
    for line in f:
        line = '\n'.join(el.strip() for el in line.split('\n') if el.strip())
        line = line.split()
        c += int(line[1]) * int(line[2])
    print(c)
