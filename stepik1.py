n = int(input())
a = [[1]]
trow = [1]
y = [0]
for _ in range(n):
    trow=[left+right for left,right in zip(trow+y, y+trow)]
    a.append(trow)
print(a[n])


'''0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
      .....'''
      