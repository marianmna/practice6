def kghnite_move(x_1, y_1, x_2, y_2):
    diff_x = abs(int(x_1) - int(x_2))
    diff_y = abs(int(y_1) - int(y_2))

    if (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1):
        return True
    else:
        return False

n, m = input().split(sep='-')

k = 'abcdefgh'
x_1 = k.index(n[0])+1
y_1 = n[1]
x_2 = k.index(m[0])+1
y_2 = m[1]

if kghnite_move(x_1, y_1, x_2, y_2):
    print('верно')
else:
    print('ошибка')
