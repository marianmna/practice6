a, b = map(int, input().split(sep='x'))
c, d, e = map(int, input().split(sep='x'))
if (c <= a and d <= b or c <= b and d <= a or c <= a and e <= b
        or c <= b and e <= a or d <= a and e <= b or d <= b and e <= a):
    print('да')
else:
    print('нет')
