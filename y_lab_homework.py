'''  ------------------------------ 
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
    return  f'''
 {a} 
{delimiter} {s} {delimiter}
 {a} '''


print(pretty_print([1, 2, 10, 23, 123, 3000]))
print(pretty_print(['abc', 'def', 'ghi', '12345']))
print(pretty_print(['abc', 'def', 'ghi'], side='*'))
print(pretty_print(['abc', 'def', 'ghi'], delimiter='#'))
print(pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#'))
