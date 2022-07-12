ph = 'numbers.txt'
with open(ph, 'r', encoding='utf-8') as f:
    a = f.read()
    new_str = '\n'.join(el.strip() for el in a.split('\n'))
    print(sum(list(map(int, new_str.split()))))
