from math import floor
a, b, n = map(int, input().split())

if b <= n:
    x = b-1
else:
    x = n

ans = floor(a*x/b) - a*floor(x/b)
print(ans)
