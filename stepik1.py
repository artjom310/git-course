import random
import string


def gen_pass_len():
    '''ф-ия генерит все символы для сборки пароля'''
    return ''.join((set(string.ascii_letters) |
                    set(string.digits)) - set('lI1oO0'))


def gen_pass_lst():
    '''генерит список пароль с заданной длинной символов'''
    n = int(input())
    m = int(input())
    lst = []
    c = 0
    while c < n:
        while True:
            password = ''.join(random.sample(gen_pass_len(), m))
            if (any(c.islower() for c in password) and any(c.isupper() for c in
                                                           password)
                    and any(c.isdigit() for c in password)):
                break
        c += 1
        lst.append(password)
    for i in lst:
        print(i)


gen_pass_lst()
