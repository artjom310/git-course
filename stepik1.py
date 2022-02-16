'''ddgd
'''

import random

addres = 'AB23_56VG'

"""AB23_56VG
"""

# функция для рандомного создания индекса


def generate_index():
    '''гребана пайлинт сцуко'''
    a = random.randint(65, 90)
    b = random.randint(65, 90)
    c = random.randint(65, 90)
    d = random.randint(65, 90)
    n = random.randrange(9)
    n1 = random.randrange(9)
    n2 = random.randrange(9)
    n3 = random.randrange(9)
    return chr(a) + chr(b) + str(n) + str(n1) + '_' + str(n2)  + str(n3) + chr(c) + chr(d)


print(generate_index())
