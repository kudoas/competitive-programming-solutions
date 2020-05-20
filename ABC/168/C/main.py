import math

a, b, h, m = map(int, input().split())

short = h/12+(m/60*1/12)
long = m/60

diff = abs(long-short)
ans = diff*360

if ans > 180:
    ans = 360-ans

total = a**2 + b**2 - 2*a*b*math.cos(math.radians(ans))
print(total**(1/2))
