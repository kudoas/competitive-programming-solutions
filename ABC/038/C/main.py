import math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = int(input())
a = list(map(int, input().split()))
a_t = [0] + [a[i + 1] - a[i] > 0 for i in range(n - 1)] + [-1]
inc = []
cnt = 0
for i in range(n + 1):
    if a_t[i] > 0:
        cnt += 1
    else:
        inc.append(cnt + 1)
        cnt = 0
ans = 0
for i in inc:
    if i >= 2:
        ans += nCr(i, 2)
ans += n
print(ans)
