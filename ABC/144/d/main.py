import math

# 場合分けあり

a, b, x = map(int, input().split())

h = x/(a**2)
men = a*h
m = men * 2/b

if men <= a*b/2:
    rad = math.atan(b/m)
    print(math.degrees(rad))
else:
    y = 2*men/a-b
    rad = math.atan((b-y)/a)
    print(math.degrees(rad))
