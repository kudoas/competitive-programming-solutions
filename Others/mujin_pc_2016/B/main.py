from math import pi

abc = sorted(list(map(int, input().split())))
a, b, c = abc

if a + b >= c:
    l = 0
elif a+b < c:
    l = c-(a+b)

ans = (a+b+c)*(a+b+c)*pi-(l*l*pi)
print(ans)
