import math

n = int(input())
se = list(set(int(input()) for _ in range(n)))
se.sort(reverse=True)
ans = 0
for i in range(len(se)):
    if i % 2 == 0:
        ans += se[i]**2
    else:
        ans -= se[i]**2
else:
    ans *= math.pi
print(ans)
