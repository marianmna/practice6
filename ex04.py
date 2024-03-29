n = input()
if int(n[1]) % 2 == 0 and (n[0] == 'a' or n[0] == 'c' or n[0] == 'e' or n[0] == 'g'):
    print('белый')
elif int(n[1]) % 2 == 1 and (n[0] == 'b' or n[0] == 'd' or n[0] == 'f' or n[0] == 'h'):
    print('белый')
else:
    print('черный')
