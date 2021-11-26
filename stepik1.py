# На вход программе подается строка текста, содержащая числа.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO,
# если не встречалось.
s = input().split()
leadingremoved = []
for i in s:
    while i[0] == "0":
        i = i[1:]
    leadingremoved.append(i)
a = set()
for i in leadingremoved:
    if i in a:
        print('YES')
        a.add(i)
    else:
        print('NO')
        a.add(i)
