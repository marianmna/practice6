n, k, m = map(int, input().split(sep=' '))
a = k*(n//k)*2*m+(n % k)*2*m
print(a)
