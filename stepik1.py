n = list(map(int, input().split()))
s = n[0]
coun = 0
for i in range(1, len(n)):
    if n[i] > s:
        coun += 1
        s = n[i]
    else:
        s = n[i]
print(coun)
