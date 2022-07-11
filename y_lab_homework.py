'''
 ------------------------------ 
| 1 | 2 | 10 | 23 | 123 | 3000 |
 ------------------------------ 
 ------------------------- 
| abc | def | ghi | 12345 |
 ------------------------- 
 ***************** 
| abc | def | ghi |
 ***************** 
 ----------------- 
# abc # def # ghi #
 ----------------- 
 ***************** 
# abc # def # ghi #
 ***************** 

'''


def pretty_print(*data, side='-', delimiter='|'):

    s = f' {delimiter} '.join(map(str, *data))
    c = 2
    for _ in s:
        c += 1
    a = f"{side}" * c
    print(f'''
 {a} 
{delimiter} {s} {delimiter}
 {a} ''', end='')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


PH = r'C:\Users\User\Desktop\eng\back_dev\git-course\image.JPG'
with open(PH, 'rb') as r:
    print(r.readline())
