a = int(input())
if 1 <= a <= 10:
    print(a - 1)
if 11 <= a <= 190:
    b = (a - 10) // 2 + 9
    if (a - 10) % 2 == 0:
        print(b % 10)
    if (a - 10) % 2 == 1:
        print((b + 1) // 10)
if 191 <= a <= 493:
    b = (a - 190) // 3 + 99
    if (a - 190) % 3 == 0:
        print((b % 100) % 10)
    if (a - 190) % 3 == 2:
        print(((b + 1) % 100) // 10)
    if (a - 190) % 3 == 1:
        print((b + 1) // 100)