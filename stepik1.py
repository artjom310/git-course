import re

'''
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
1 2 7 8'''

lst = {x: input() for x in range(1, int(input()) + 1)}
print(lst)
regex = ''.join(f'.*?{i}' for i in 'anton')
a = []
for k, v in lst.items():
    if re.search(regex, v):
        a.append(k)
print(*a)
