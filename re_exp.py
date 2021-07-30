import re

regex = ''.join(f'.*?{i}' for i in 'anton')
a = []
n = 1
lst = [input() for i in range(int(input()))]
for i in lst:
    if re.search(regex, i):
        a.append(n)
        n += 1
    else:
        a.append(0)
print(a)

'''
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
'''