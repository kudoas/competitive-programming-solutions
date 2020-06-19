from collections import Counter


c = Counter(input())
t = int(input())
x = abs(c['R']-c['L'])
y = abs(c['U']-c['D'])

if t == 1:
    ans = x+y+c['?']
else:
    z = c['?']
    if z > x+y:
        ans = (z-x-y) % 2
    else:
        ans = x+y-z
print(ans)
