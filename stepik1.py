from itertools import groupby
lst = []
s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
s = s.split()
s = groupby(s)
for i , j in s:
    lst.append(list(j))
print(lst)

'''На вход программе подается строка текста, содержащая символы. Напишите программу, 
которая упаковывает последовательности одинаковых символов заданной строки в подсписки.'''