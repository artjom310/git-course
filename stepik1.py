import random
import string

'''LETTER = ''.join((set(string.ascii_letters) |
                 set(string.digits)) - set('lI1oO0'))
n = int(input())
length = int(input())  # длина пароля
for i in range(n):
    print(''.join(random.sample(LETTER, length)))
'''
n = int(input())
m = int(input())


def gen_pass_len():
    '''ф-ия генерит все символы для сборки пароля'''
    return ''.join((set(string.ascii_letters) |
                    set(string.digits)) - set('lI1oO0'))


def gen_pass_lst(count, lenght):
    '''генерит список пароль с заданной длинной символов'''
    for _ in range(count):
        print(''.join(random.sample(gen_pass_len(), lenght)))


gen_pass_lst(n, m)
